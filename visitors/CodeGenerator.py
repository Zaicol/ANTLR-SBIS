from bisect import bisect_left
from typing import Any

from generated.ASICParser import ASICParser
from generated.ASICParserVisitor import ASICParserVisitor
from models.BitCommand import BitCommand
from models.BitInstruction import BitInstruction
from models.BitConfig import BitConfig
from models.Constant import Constant
from models.Label import Label
from models.LastInstruction import LastInstruction
from models.enums.ConfigEnums import InputName, BPDAddress
from models.enums.InstructionEnums import *
from utils.utils import raise_syntax_error, raise_undefined_error
from visitors.ExpressionEvaluator import ExpressionEvaluator


class CodeGenerator(ASICParserVisitor):
    labels: dict[str, Label] = {}  # Метки и их адреса
    configs: dict[str, int] = {}  # Конфигурации и их индексы
    defines: dict[str, Any] = {}  # Макросы и их значения
    constants: dict[str, Constant] = {}
    config_code: list[BitConfig] = []  # Список конфигураций (128 бит)
    machine_code: list[BitCommand] = []  # Список инструкций (32 бита)
    for_loops: list[str] = []  # Список циклов
    expr_evaluator: ExpressionEvaluator  # Объект для вычисления выражений

    def __init__(self, labels: dict[str, Label], configs: dict[str, int],
                 defines: dict[str, ASICParser.ExpressionContext],
                 constant_contexts: dict[str, ASICParser.Const_exprContext]):
        self.expr_evaluator = ExpressionEvaluator(defines, labels)

        self.labels = labels
        self.configs = configs

        self.config_code = []
        self.machine_code = []
        self.for_loops = []

        # Информация для вставки wait
        self.wait_inserts = []
        self.last_active_standard_instruction: LastInstruction | None = None
        self.last_passive_standard_instruction: LastInstruction | None = None
        self.last_v4_instruction: LastInstruction | None = None
        self.last_wrout_instruction: LastInstruction | None = None

        for name, const in constant_contexts.items():
            self.constants[name] = self.visit(const)

    def visitInstruction(self, ctx: ASICParser.InstructionContext):
        self.machine_code.append(BitCommand(source_line=ctx.start.line))
        self.visitChildren(ctx)
        self.check_latencies()

    def visitDefine_def(self, ctx: ASICParser.Define_defContext):
        return

    def visitSreg(self, ctx: ASICParser.SregContext):
        return ServiceRegister[ctx.getText().upper()]

    def visitAsignment(self, ctx: ASICParser.AsignmentContext):
        if ctx.arg():
            self.get_current_instruction().set_service_operation_type(ServiceType.REG_ASSIGN)
            arg_num = self.visit(ctx.arg())
            self.get_current_instruction().set_arg_num(arg_num)
        elif ctx.expression():
            self.get_current_instruction().set_service_operation_type(ServiceType.REG_INIT)
            expr_value = self.calc_expr(ctx.expression(), 24)
            self.get_current_instruction().set_reg_init_value(expr_value)
        self.get_current_instruction().set_service_reg(self.visit(ctx.sreg()))
        return

    def visitArg(self, ctx: ASICParser.ArgContext):
        arg_num = int(ctx.getText()[1])
        if not (0 <= arg_num <= 3):
            raise_syntax_error(f"Invalid argument number: {arg_num}", ctx)
        return arg_num

    def visitSregop(self, ctx: ASICParser.SregopContext):
        self.get_current_instruction().set_operation_type(InstructionType.SERVICE)
        return self.visitChildren(ctx)

    def visitAluSpOp(self, ctx: ASICParser.AluSpOpContext):
        # Стандартная команда
        self.get_current_instruction().set_operation_type(InstructionType.STANDARD)
        return self.visitChildren(ctx)

    def visitGenOp(self, ctx: ASICParser.GenOpContext):
        # v1 = gen
        self.get_current_instruction().set_operation_type(InstructionType.STANDARD)
        self.get_current_instruction().set_start_gen()
        return

    def visitSpCop(self, ctx: ASICParser.SpCopContext):
        self.get_current_instruction().set_operation_type(InstructionType.SERVICE)
        return self.visitChildren(ctx)

    def visitEop(self, ctx: ASICParser.EopContext):
        # eop
        self.get_current_instruction().set_eop()
        return

    def visitWait(self, ctx: ASICParser.WaitContext):
        # wait(expression)
        self.get_current_instruction().set_wait()
        return self.visitChildren(ctx)

    def visitJump(self, ctx: ASICParser.JumpContext):
        # jnz(sreg, label)
        self.get_current_instruction().set_service_operation_type(ServiceType.JNZ)
        self.get_current_instruction().set_service_reg(self.visit(ctx.sreg()))
        label_name = ctx.label().getText()
        label = self.labels.get(label_name, None)
        if label is None:
            raise_undefined_error(identifier=label_name, ctx=ctx)
        self.get_current_instruction().set_label_addr(label.address)
        self.get_current_instruction().set_jump_label(label)
        return

    def visitExpression(self, ctx: ASICParser.ExpressionContext):
        value: int = self.expr_evaluator.visit_line(ctx)
        self.get_current_instruction().set_expression_value(value)
        return self.expr_evaluator.visit(ctx)

    def visitArith(self, ctx: ASICParser.ArithContext):
        # r0++
        self.get_current_instruction().set_service_operation_type(ServiceType.INC_DEC)
        if ctx.MINUSMINUS():
            self.get_current_instruction().set_service_reg(self.visit(ctx.sreg()))
            self.get_current_instruction().set_decrement()
        elif ctx.PLUSPLUS():
            self.get_current_instruction().set_service_reg(ServiceRegister.R0)
            self.get_current_instruction().set_increment()

    def visitResultexpr(self, ctx: ASICParser.ResultexprContext):
        outputs: list[ASICParser.OutputContext] = ctx.output()
        output_places: list[OutputPlaces] = []
        for output in outputs:
            place = self.visit(output)
            if place is not None:
                output_places.append(place)
        if len(output_places) > 5:
            raise_syntax_error(f"Too many outputs ({len(output_places)} > 5)", ctx)
        self.get_current_instruction().set_output(output_places)
        return

    def visitOutput(self, ctx: ASICParser.OutputContext) -> OutputPlaces | None:
        ctx_text = ctx.getText()
        try:
            return OutputPlaces[ctx_text.upper().replace("^", "N").replace("&", "M")]
        except KeyError:
            raise ValueError(f"Неподдерживаемый выход: {ctx_text}")

    def visitResultout(self, ctx: ASICParser.ResultoutContext):
        self.get_current_instruction().set_wrout()
        return

    def visitStdop(self, ctx: ASICParser.StdopContext):
        ctx_text = ctx.start.text
        try:
            sp_type = SPType[ctx_text.upper()]
        except KeyError:
            raise ValueError(f"Неподдерживаемый spop: {ctx_text}")
        self.get_current_instruction().set_sp_op(sp_type)
        return self.visitChildren(ctx)

    def visitAluop(self, ctx: ASICParser.AluopContext):
        ctx_text = ctx.start.text
        try:
            alu_type = ALUType[ctx_text.upper()]
        except KeyError:
            raise ValueError(f"Неподдерживаемый aluop: {ctx_text}")
        self.get_current_instruction().set_alu_op(alu_type)
        return self.visitChildren(ctx)

    def visitConfig_name(self, ctx: ASICParser.Config_nameContext):
        if not isinstance(ctx.parentCtx, ASICParser.Config_defContext):
            config_name = ctx.getText()
            if config_name not in self.configs:
                raise_undefined_error(identifier=config_name, ctx=ctx)
            self.get_current_instruction().set_config_addr(self.configs[config_name])
        return self.visitChildren(ctx)

    def visitConfig_def(self, ctx: ASICParser.Config_defContext):
        self.config_code.append(BitConfig(source_line=ctx.start.line))
        return self.visitChildren(ctx)

    def visitVreg_d(self, ctx: ASICParser.Vreg_dContext):
        return BPDAddress[ctx.getText().upper()]

    def visitConst_expr(self, ctx: ASICParser.Const_exprContext) -> Constant:
        constant = Constant()
        if ctx.const_addr():
            addr_ctx: ASICParser.Const_addrContext = ctx.const_addr()
            if addr_ctx.expression():
                constant.set_address(self.calc_expr(ctx.const_addr().expression(), 7))
            elif addr_ctx.sreg():
                constant.set_reg(self.visit(addr_ctx.sreg()))
            elif addr_ctx.vreg_d():
                constant.set_bpd(self.visit(addr_ctx.vreg_d()))
        if ctx.const_shift():
            constant.set_shift(self.calc_expr(ctx.const_shift().expression()))
        return constant

    def visitConst_name(self, ctx: ASICParser.Const_nameContext) -> Constant:
        const_name = ctx.getText()
        if const_name not in self.constants:
            raise_undefined_error(identifier=const_name, ctx=ctx)
        constant: Constant = self.constants[const_name]
        return constant

    def visitConf_c(self, ctx: ASICParser.Conf_cContext):
        if ctx.const_expr():
            constant: Constant = self.visit(ctx.const_expr())
        elif ctx.const_name():
            constant: Constant = self.visit(ctx.const_name())
        else:
            raise_syntax_error(f"Unknown type of constant in config: {ctx.getText()}", ctx)
        self.config_code[-1].set_constant(constant)
        return

    def visitConf_d(self, ctx: ASICParser.Conf_dContext):
        shift_value = None  # sh_R1-sh_R4
        significant_count = 32  # tr_R1-tr_R4

        # Получаем название входа: v1, v1h, v2, v3, v4, r0, rev(r0)
        if ctx.vreg():
            reg_name = InputName[ctx.vreg().getText().upper()]
        elif ctx.vreg_r():
            if ctx.vreg_r().REV_REG():
                # Если вход - rev_reg(r0), то устанавливается соответствующий флаг
                self.config_code[-1].set_rev_reg()
            reg_name = InputName.R0
            significant_count = 64
        else:
            raise Exception("Unknown vreg")

        if len(ctx.expression()) == 2:
            # input{significant_count} << shift
            significant_count = self.calc_expr(ctx.expression(0))
            shift_value = self.calc_expr(ctx.expression(1))
        elif ctx.LSHIFT():
            # input << shift
            shift_value = self.calc_expr(ctx.expression(0))
        elif len(ctx.expression()) > 0:
            # input{significant_count}
            significant_count = self.calc_expr(ctx.expression(0))

        # Вызываем метод BitConfig.set_input, который устанавливает нужные значения в подходящих позициях
        self.config_code[-1].set_input(reg_name, shift_value, significant_count)
        return

    def visitRev_configuration(self, ctx: ASICParser.Rev_configurationContext):
        self.config_code[-1].set_rev_txt()
        return self.visitChildren(ctx)

    def visitArgument(self, ctx: ASICParser.ArgumentContext):
        if ctx.configuration():
            self.config_code.append(BitConfig(source_line=ctx.start.line))
            self.get_current_instruction().set_config_addr(len(self.config_code) - 1)
        return self.visitChildren(ctx)

    def check_latencies(self):
        """
        Вставляет wait, если требуется
        """
        if len(self.machine_code) == 0:
            return

        instr = self.get_current_instruction()
        instr_idx = len(self.machine_code) - 1
        self.check_active_standard_latency(instr, instr_idx)
        self.check_passive_standard_latency(instr, instr_idx)
        self.check_wrout_latency(instr, instr_idx)
        self.check_wait_latency(instr)

    def check_active_standard_latency(self, instr: BitCommand, instr_idx: int):
        if not instr.is_active_standard():
            return

        lat = 0

        # Интервал между операциями должен быть не менее 64+max{0, L1-L2} тактов
        last: LastInstruction | None = self.last_active_standard_instruction
        if last is not None:
            l1 = last.get_instruction().get_latency()
            l2 = instr.get_latency()
            lat = 64 + max(0, l1 - l2) - last.get_cycles_since()

        # при выдаче векторного регистра v4 в выходной поток,
        # нельзя писать в регистр v4 на протяжении 256 тактов.
        last_wrout: LastInstruction | None = self.last_wrout_instruction
        has_v4 = instr.has_v4_in_outputs()
        if has_v4 and last_wrout is not None:
            l1 = last_wrout.get_instruction().get_latency()
            v4_lat = 256 + l1 - last_wrout.get_cycles_since()
            if v4_lat > lat:
                lat = v4_lat

        if lat > 0:
            self.wait_inserts.append((instr_idx, lat))

        self.last_active_standard_instruction = LastInstruction(idx=instr_idx, instruction=instr)
        if has_v4:
            self.last_v4_instruction = LastInstruction(idx=instr_idx, instruction=instr)

    def check_passive_standard_latency(self, instr: BitCommand, instr_idx: int):
        if not instr.is_passive_standard():
            return

        lat = 0
        # Пассивную стандартную инструкцию можно выполнять вслед за активной
        # на интервале менее 64 тактов при условии повторения полей cmd[21..12].
        last: LastInstruction | None = self.last_active_standard_instruction
        if last is not None and not instr.check_same_instructions(last.get_instruction()):
            l1 = last.get_instruction().get_latency()
            l2 = instr.get_latency()
            lat = 64 + max(0, l1 - l2) - last.get_cycles_since()

        if lat > 0:
            self.wait_inserts.append((instr_idx, lat))

        self.last_passive_standard_instruction = LastInstruction(idx=instr_idx, instruction=instr)

    def check_wrout_latency(self, instr: BitCommand, instr_idx: int):
        if not instr.is_wrout():
            return

        lat = 0
        # После формирования пакета данных для v4 следует выдержать
        # интервал не менее L+5 тактов перед записью в out
        last: LastInstruction | None = self.last_v4_instruction
        if last is not None:
            l1 = last.get_instruction().get_latency()
            lat = 5 + l1 - last.get_cycles_since()

        if lat > 0:
            self.wait_inserts.append((instr_idx, lat))

        self.last_wrout_instruction = LastInstruction(idx=instr_idx, instruction=instr)

    def check_wait_latency(self, instr: BitCommand):
        if not (cycles := instr.get_wait()):
            return

        if self.last_active_standard_instruction is not None:
            self.last_active_standard_instruction.add_cycles(cycles)

        if self.last_passive_standard_instruction is not None:
            self.last_passive_standard_instruction.add_cycles(cycles)

        if self.last_v4_instruction is not None:
            self.last_v4_instruction.add_cycles(cycles)

        if self.last_wrout_instruction is not None:
            self.last_wrout_instruction.add_cycles(cycles)

    def update_labels(self):
        source_line_to_instruction_map = self.get_source_line_to_instruction_map()
        for label in self.labels.values():
            label.address = self.get_closest_line(source_line_to_instruction_map, label.source_line)

        for instruction in self.machine_code:
            if instruction.is_jump():
                instruction.set_expression_value(self.labels[instruction.get_jump_label().name].address)

    def get_closest_line(self, source_line_map: dict[int, int], source_line: int) -> int:
        if source_line in source_line_map:
            return source_line_map[source_line]

        keys = sorted(source_line_map.keys())
        i = bisect_left(keys, source_line)

        closest_next_line = keys[i] if i < len(keys) else None

        if closest_next_line is None:
            raise_syntax_error(f"Can't find closest instruction for source line: {source_line}", None)

        return source_line_map[closest_next_line]

    def get_source_line_to_instruction_map(self) -> dict[int, int]:
        result = {}
        for i, instruction in enumerate(self.machine_code):
            sl = instruction.get_source_line()
            if sl in result:
                result[sl] = min(result[sl], i)
            else:
                result[sl] = i
        return result

    # ====== Методы для вывода кода ======

    def get_machine_code(self) -> list[BitInstruction]:
        return self.machine_code

    def get_config_code(self) -> list[BitConfig]:
        return self.config_code

    def get_full_code_hex(self, prefix=False,
                          show_source_line=False,
                          split_bytes=False) -> list[str]:
        result = [f"#conf {len(self.config_code)}"]
        prefix_str = "0x" if prefix else ""
        for config in self.config_code:
            source_line = f"{config.source_line}:\t" if show_source_line else ""
            conf_hex = config.to_hex(False, split_bytes)
            result += [source_line + prefix_str + conf_hex[i] for i in range(4)]

        result += [f"#prog {len(self.machine_code)}"]
        for instruction in self.machine_code:
            source_line = f"{instruction.source_line}:\t" if show_source_line else ""
            inst_hex = instruction.to_hex_str(False, split_bytes)
            result.append(source_line + prefix_str + inst_hex)
        return result

    def get_full_code_binary(self, prefix=False, show_source_line=False) -> list[str]:
        result = [f"#conf {len(self.config_code)}"]
        prefix_str = "0x" if prefix else ""
        for config in self.config_code:
            source_line = f"{config.source_line}:\t" if show_source_line else ""
            config_bin_list = config.to_binary_list()
            result += [source_line + prefix_str + config_bin_list[i] for i in range(4)]

        result += [f"#prog {len(self.machine_code)}"]
        for instruction in self.machine_code:
            source_line = f"{instruction.source_line}:\t" if show_source_line else ""
            instruction_bin_list = instruction.to_binary_list()
            result.append(source_line + prefix_str + instruction_bin_list[0])
        return result

    def get_full_code_hex_str(self, prefix=False,
                              show_source_line=False,
                              split_bytes=False) -> str:
        code = self.get_full_code_hex(prefix, show_source_line, split_bytes)
        return "\n".join(code)

    def get_full_code_binary_str(self, prefix=False, show_source_line=False) -> str:
        code = self.get_full_code_binary(prefix, show_source_line)
        return "\n".join(code)

    def get_current_instruction(self) -> BitCommand | None:
        if len(self.machine_code) == 0:
            return None
        return self.machine_code[-1]

    def calc_expr(self, ctx: ASICParser.ExpressionContext, max_size_in_bits: int = 8) -> int:
        return self.expr_evaluator.visit_line(ctx, max_size_in_bits)
