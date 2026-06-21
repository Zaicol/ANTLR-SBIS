from bisect import bisect_left
from typing import Any

from generated.ASICParser import ASICParser
from generated.ASICParserVisitor import ASICParserVisitor
from models.BitCommand import BitCommand
from models.BitInstruction import BitInstruction
from models.BitConfig import BitConfig
from models.Constant import Constant
from models.Label import Label
from models.enums.InstructionEnums import *
from models.exceptions.AssemblerSyntaxError import AssemblerSyntaxError
from models.exceptions.AssemblerUndefinedError import AssemblerUndefinedError
from visitors.ExpressionEvaluator import ExpressionEvaluator


class CodeGenerator(ASICParserVisitor):
    labels: dict[str, Label] = {}  # Метки и их адреса
    configs: dict[str, int] = {}  # Конфигурации и их индексы
    defines: dict[str, Any] = {}  # Макросы и их значения
    constants: dict[str, Constant] = {}
    config_code: list[BitConfig] = []  # Список конфигураций (128 бит)
    machine_code: list[BitCommand] = []  # Список инструкций (32 бита)
    for_loops: list[str] = []  # Список циклов
    current_source_line: int = 0  # Текущая строка исходного кода
    expr_evaluator: ExpressionEvaluator  # Объект для вычисления выражений

    def __init__(self, labels: dict[str, Label], configs: dict[str, int],
                 defines: dict[str, ASICParser.ExpressionContext],
                 constant_contexts: dict[str, ASICParser.Const_exprContext]):
        self.expr_evaluator = ExpressionEvaluator(defines, self.current_source_line, labels)

        self.labels = labels
        self.configs = configs
        for name, const in constant_contexts.items():
            self.constants[name] = self.visit(const)

        self.config_code = []
        self.machine_code = []
        self.for_loops = []
        self.current_source_line = 0

    def visitDefine_def(self, ctx: ASICParser.Define_defContext):
        return

    def visitSreg(self, ctx: ASICParser.SregContext):
        regs = {
            "r0": ServiceRegister.R0,
            "r1": ServiceRegister.R1,
            "r2": ServiceRegister.R2,
            "r3": ServiceRegister.R3
        }
        self.get_current_instruction().set_service_reg(regs[ctx.getText()])
        return regs[ctx.getText()]

    def visitAsignment(self, ctx: ASICParser.AsignmentContext):
        if ctx.arg():
            self.get_current_instruction().set_service_operation_type(ServiceType.REG_ASSIGN)
            arg_num = self.visit(ctx.arg())
            self.get_current_instruction().set_arg_num(arg_num)
        elif ctx.expression():
            self.get_current_instruction().set_service_operation_type(ServiceType.REG_INIT)
            expr_value = self.calc_expr(ctx.expression(), 24)
            self.get_current_instruction().set_reg_init_value(expr_value)
        self.visit(ctx.sreg())
        return

    def visitArg(self, ctx: ASICParser.ArgContext):
        arg_num = int(ctx.getText()[1])
        if not (0 <= arg_num <= 3):
            raise AssemblerSyntaxError(f"Invalid argument number: {arg_num}", self.current_source_line)
        return arg_num

    def visitSregop(self, ctx: ASICParser.SregopContext):
        self.get_current_instruction().set_operation_type(InstructionType.SERVICE)
        return self.visitChildren(ctx)

    def visitAluSpOp(self, ctx: ASICParser.AluSpOpContext):
        # Стандартная команда
        self.get_current_instruction().set_operation_type(InstructionType.STANDARD)
        return self.visitChildren(ctx)

    def visitSpCopOp(self, ctx: ASICParser.SpCopOpContext):
        # Стандартная команда
        self.get_current_instruction().set_operation_type(InstructionType.STANDARD)
        if ctx.spcop().getText() == 'gen':
            self.get_current_instruction().set_start_gen()
            if ctx.resultexpr().getText() != 'v1':
                raise AssemblerSyntaxError("gen operation can be used only with v1 register",
                                           self.current_source_line)
            return
        return self.visitChildren(ctx)

    def visitSpCopOnly(self, ctx: ASICParser.SpCopOnlyContext):
        if ctx.getText() == 'eop':
            self.get_current_instruction().set_eop()
        else:
            self.get_current_instruction().set_operation_type(InstructionType.SERVICE)
        return self.visitChildren(ctx)

    def visitSpcop(self, ctx: ASICParser.SpcopContext):
        ctx_text = ctx.start.text
        if ctx_text == 'gen':
            # start_gen – запуск генерации очередного пакета данных
            self.get_current_instruction().set_start_gen()
        elif ctx_text == 'wait':
            self.get_current_instruction().set_wait()
        elif ctx_text == 'jnz':
            # Условный переход
            self.get_current_instruction().set_service_operation_type(ServiceType.JNZ)
        return self.visitChildren(ctx)

    def visitJump(self, ctx: ASICParser.JumpContext):
        self.get_current_instruction().set_service_operation_type(ServiceType.JNZ)
        self.visit(ctx.sreg())
        label_name = ctx.label().getText()
        label = self.labels.get(label_name, None)
        if label is None:
            raise AssemblerUndefinedError(label_name, line=self.current_source_line)
        self.get_current_instruction().set_label_addr(label.address)
        self.get_current_instruction().set_jump_label(label)
        return

    def visitExpression(self, ctx: ASICParser.ExpressionContext):
        value: int = self.expr_evaluator.visit_line(ctx, self.current_source_line)
        self.get_current_instruction().set_expression_value(value)
        return self.expr_evaluator.visit(ctx)

    def visitArith(self, ctx: ASICParser.ArithContext):
        op = ctx.getChild(1).getText()
        self.get_current_instruction().set_service_operation_type(ServiceType.INC_DEC)
        if op == '--':
            self.get_current_instruction().set_decrement()
        elif op == '++':
            self.get_current_instruction().set_increment()
        return self.visitChildren(ctx)

    def visitResultexpr(self, ctx: ASICParser.ResultexprContext):
        outputs: list[ASICParser.OutputContext] = ctx.output()
        output_places: list[OutputPlaces] = []
        for output in outputs:
            place = self.visit(output)
            if place is not None:
                output_places.append(place)
        if len(output_places) > 5:
            raise AssemblerSyntaxError(f"Too many outputs ({len(output_places)} > 5)", self.current_source_line)
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
                raise AssemblerUndefinedError(config_name, line=self.current_source_line)
            self.get_current_instruction().set_config_addr(self.configs[config_name])
        return self.visitChildren(ctx)

    def visitInstruction(self, ctx: ASICParser.InstructionContext):
        self.machine_code.append(BitCommand(source_line=self.current_source_line))
        return self.visitChildren(ctx)

    def visitLine(self, ctx: ASICParser.LineContext):
        self.current_source_line += 1
        return self.visitChildren(ctx)

    def visitConfig_def(self, ctx: ASICParser.Config_defContext):
        self.config_code.append(BitConfig(source_line=self.current_source_line))
        return self.visitChildren(ctx)

    def visitConst_expr(self, ctx: ASICParser.Const_exprContext) -> Constant:
        const_addr = self.calc_expr(ctx.expression()[0])
        constant = Constant(const_addr)
        if ctx.LSHIFT():
            constant.set_shift(self.calc_expr(ctx.expression()[1]))
        return constant

    def visitConst_name(self, ctx: ASICParser.Const_nameContext) -> Constant:
        const_name = ctx.getText()
        if const_name not in self.constants:
            raise AssemblerUndefinedError(const_name, line=self.current_source_line)
        constant: Constant = self.constants[const_name]
        return constant

    def visitConf_c(self, ctx: ASICParser.Conf_cContext):
        if ctx.const_expr():
            constant: Constant = self.visit(ctx.const_expr())
        elif ctx.const_name():
            constant: Constant = self.visit(ctx.const_name())
        else:
            raise AssemblerSyntaxError("Unknown conf_c", self.current_source_line)
        self.config_code[-1].set_constant(constant.get_address(), constant.get_shift())
        return

    def visitConf_d(self, ctx: ASICParser.Conf_dContext):
        shift_value = None  # sh_R1-sh_R4
        significant_count = 32  # tr_R1-tr_R4

        # Получаем название входа: v1, v1h, v2, v3, v4, r0, rev(r0)
        if ctx.vreg():
            reg_name = ctx.vreg().getText()
        elif ctx.vreg_r():
            if ctx.vreg_r().REV():
                # Если вход - rev(r0), то устанавливается соответствующий флаг
                self.config_code[-1].set_rev_reg()
            reg_name = ctx.vreg_r().R0().getText()
            significant_count = 64
        else:
            raise Exception("Unknown vreg")

        if len(ctx.expression()) == 2:
            # input{significant_count} << shift
            significant_count = int(ctx.expression()[0].getText())
            shift_value = int(ctx.expression()[1].getText())
        elif ctx.LSHIFT():
            # input << shift
            shift_value = int(ctx.expression()[0].getText())
        elif len(ctx.expression()) > 0:
            # input{significant_count}
            significant_count = int(ctx.expression()[0].getText())

        # Вызываем метод BitConfig.set_input, который устанавливает нужные значения в подходящих позициях
        self.config_code[-1].set_input(reg_name, shift_value, significant_count)
        return

    def visitRev_configuration(self, ctx: ASICParser.Rev_configurationContext):
        self.config_code[-1].set_rev_txt()
        return self.visitChildren(ctx)

    def visitArgument(self, ctx:ASICParser.ArgumentContext):
        if ctx.configuration():
            self.config_code.append(BitConfig(source_line=self.current_source_line))
            self.get_current_instruction().set_config_addr(len(self.config_code) - 1)
        return self.visitChildren(ctx)

    def visitForloop(self, ctx: ASICParser.ForloopContext):
        # TODO: Реализовать
        return

    def insert_wait_instructions(self):
        def is_wait_next(index: int) -> bool:
            if len(self.machine_code) > index + 1:
                return False
            return self.machine_code[index].is_wait()

        def make_wait_instruction(cycles: int, source_line: int) -> BitCommand:
            new_instruction = BitCommand(source_line=source_line)
            new_instruction.set_wait()
            new_instruction.set_expression_value(cycles)
            return new_instruction

        result = []
        last_active_index = -1

        for i, instruction in enumerate(self.machine_code):

            result.append(instruction)

            if instruction.is_start_gen():
                if is_wait_next(i):
                    self.machine_code[i].set_expression_value(max(self.machine_code[i].get_wait(), 4))
                else:
                    result.append(make_wait_instruction(4, instruction.get_source_line()))
                continue

            if instruction.is_wrout():
                if is_wait_next(i):
                    self.machine_code[i].set_expression_value(max(self.machine_code[i].get_wait(), 5))
                else:
                    result.append(make_wait_instruction(5, instruction.get_source_line()))
                continue

            if instruction.is_active_standard():
                if last_active_index != -1:
                    gap = len(result) - last_active_index - 1

                    if gap < 128:
                        needed = 128 - gap
                        result.append(make_wait_instruction(needed, instruction.get_source_line()))

                last_active_index = len(result) - 1
                continue

        self.machine_code = result
        self.update_labels()

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
            raise AssemblerSyntaxError(f"Can't find closest instruction for source line: {source_line}", source_line)

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

    def get_current_instruction(self) -> BitCommand:
        return self.machine_code[-1]

    def calc_expr(self, ctx: ASICParser.ExpressionContext, max_size_in_bits: int = 8) -> int:
        return self.expr_evaluator.visit_line(ctx, self.current_source_line, max_size_in_bits)
