from generated.ASICLexer import ASICLexer
from generated.ASICParser import ASICParser
from generated.ASICParserVisitor import ASICParserVisitor
from models.BitInstruction import BitInstruction
from models.BitConfig import BitConfig


def stdop_match(ctx_text):
    match ctx_text:
        case "a1":
            return 0
        case "a4":
            return 1
        case "a5":
            return 2
        case "a128d":
            return 3
        case "d":
            return 4
        case "dinv":
            return 5


def aluop_match(ctx_text):
    # (0 – A; 1 – A and B; 2 – A or B; 3 – A xor B; 4 – not A; 5 – rev(A))
    match ctx_text:
        case "and":
            return 1
        case "or":
            return 2
        case "xor":
            return 3
        case "not":
            return 4
        case "rev":
            return 5
    return 0


class CodeGenerator(ASICParserVisitor):
    labels: dict[str, int] = {}              # Метки и их адреса
    configs: dict[str, int] = {}             # Конфигурации и их индексы
    config_code: list[BitConfig] = []        # Список конфигураций (128 бит)
    machine_code: list[BitInstruction] = []  # Список инструкций (32 бита)
    for_loops: list[str] = []                # Список циклов
    current_source_line: int = 0             # Текущая строка исходного кода

    def __init__(self, labels, configs):
        self.labels = labels
        self.configs = configs
        self.config_code = []
        self.machine_code = []
        self.for_loops = []
        self.current_source_line = 0

    def visitSreg(self, ctx: ASICParser.SregContext):
        regs = {
            "r0": '00',
            "r1": '01',
            "r2": '10',
            "r3": '11'
        }
        self.machine_code[-1][29:28] = regs[ctx.getText()]
        return self.visitChildren(ctx)

    def visitAsignment(self, ctx: ASICParser.AsignmentContext):
        self.machine_code[-1][26:25] = '10'
        return self.visitChildren(ctx)

    def visitArg(self, ctx: ASICParser.ArgContext):
        self.machine_code[-1][1:0] = format(int(ctx.getText()[1]), '02b')
        return self.visitChildren(ctx)

    def visitSregop(self, ctx: ASICParser.SregopContext):
        # Служебная команда:
        #   Инициализация r0, r1, r2, r3
        #   Инкремент и декремент r0, r1, r2, r3
        #   Условный переход
        #   Циклы
        #   Задержка
        #   Конец программы
        self.machine_code[-1][24] = '0'
        return self.visitChildren(ctx)

    def visitAluSpOp(self, ctx: ASICParser.AluSpOpContext):
        # Стандартная команда
        self.machine_code[-1][24] = '1'
        return self.visitChildren(ctx)

    def visitSpCopOp(self, ctx: ASICParser.SpCopOpContext):
        # Стандартная команда
        self.machine_code[-1][24] = '1'
        return self.visitChildren(ctx)

    def visitSpCopOnly(self, ctx: ASICParser.SpCopOnlyContext):
        if ctx.getText() == 'eop':
            self.machine_code[-1][31] = '1'
        else:
            self.machine_code[-1][24] = '0'
        return self.visitChildren(ctx)

    def visitSpcop(self, ctx: ASICParser.SpcopContext):
        ctx_text = ctx.start.text
        if ctx_text == 'gen':
            # start_gen – запуск генерации очередного пакета данных
            self.machine_code[-1][0] = '1'
        elif ctx_text == 'wait':
            # Признак паузы: следующие cmd[7..0] тактов процес-сор не обрабатывает инструкции
            self.machine_code[-1][27] = '1'
        elif ctx_text == 'jnz':
            # Условный переход
            self.machine_code[-1][26:25] = '11'
        return self.visitChildren(ctx)

    def visitLabel(self, ctx: ASICParser.LabelContext):
        # Отделяем определение метки от её использования
        if not isinstance(ctx.parentCtx, ASICParser.LblContext):
            if not ctx.getText() in self.labels:
                raise Exception("Метка " + ctx.getText() + " не определена")
            self.machine_code[-1][7:0] = format(self.labels[ctx.getText()], '08b')
        return self.visitChildren(ctx)

    def visitConstant(self, ctx: ASICParser.ConstantContext):
        token = ctx.getChild(0).getSymbol()
        token_type = token.type
        text = ctx.getText()
        text_up = text.upper()

        if token_type == ASICLexer.HEXADECIMAL:
            if text_up.endswith('H'):
                num_part = text[:-1]
            else:  # начинается с 0x или 0X
                num_part = text[2:]
            value = int(num_part, 16)

        elif token_type == ASICLexer.BINARY:
            if text_up.endswith('B'):
                num_part = text[:-1]
            else:  # начинается с 0b или 0B
                num_part = text[2:]
            value = int(num_part, 2)

        elif token_type == ASICLexer.OCTAL:
            if text_up.endswith('O'):
                num_part = text[:-1]
            else:  # начинается с 0o или 0O
                num_part = text[2:]
            value = int(num_part, 8)

        elif token_type == ASICLexer.DECIMAL:
            if text_up.endswith('D'):
                num_part = text[:-1]
            elif text_up.startswith('0D'):
                num_part = text[2:]
            else:
                num_part = text
            value = int(num_part, 10)

        else:
            raise ValueError(f"Неизвестный тип константы: {text}")

        if not (0 <= value <= 255):
            raise ValueError(f"Константа {text} не помещается в 8 бит (допустимый диапазон: 0–255)")

        self.machine_code[-1][7:0] = format(value, '08b')
        return self.visitChildren(ctx)

    def visitArith(self, ctx: ASICParser.ArithContext):
        op = ctx.getChild(1).getText()
        self.machine_code[-1][25] = '1'
        if op == '--':
            self.machine_code[-1][30] = '0'
        elif op == '++':
            self.machine_code[-1][30] = '1'
        return self.visitChildren(ctx)

    def visitOutput(self, ctx: ASICParser.OutputContext):
        ctx_text = ctx.start.text
        bit_index = 0
        match ctx_text:
            case "v1":
                bit_index = 16
            case "v2":
                bit_index = 17
            case "v3":
                bit_index = 18
            case "v4":
                bit_index = 19
            case "v2^":
                bit_index = 20
            case "v4&":
                bit_index = 21
            case "cmp":
                bit_index = 3
            case _:
                raise ValueError(f"Неподдерживаемый выход: {ctx_text}")
        self.machine_code[-1][bit_index] = '1'
        return self.visitChildren(ctx)

    def visitResultout(self, ctx: ASICParser.ResultoutContext):
        self.machine_code[-1][1] = '1'
        return

    def visitStdop(self, ctx: ASICParser.StdopContext):
        ctx_text = ctx.start.text
        self.machine_code[-1][14:12] = format(stdop_match(ctx_text), '03b')
        return self.visitChildren(ctx)

    def visitAluop(self, ctx: ASICParser.AluopContext):
        ctx_text = ctx.start.text
        self.machine_code[-1][14:12] = format(aluop_match(ctx_text), '03b')
        return self.visitChildren(ctx)

    def visitConfig_name(self, ctx: ASICParser.Config_nameContext):
        if not isinstance(ctx.parentCtx, ASICParser.Config_defContext):
            if not ctx.getText() in self.configs:
                raise Exception("Конфигурация " + ctx.getText() + " не определена")
            self.machine_code[-1][9:4] = format(self.configs[ctx.getText()], '06b')
        return self.visitChildren(ctx)

    def visitInstruction(self, ctx: ASICParser.InstructionContext):
        self.current_source_line += 1
        self.machine_code.append(BitInstruction(source_line=self.current_source_line))
        return self.visitChildren(ctx)

    def visitDefinition(self, ctx: ASICParser.DefinitionContext):
        self.current_source_line += 1
        self.config_code.append(BitConfig(source_line=self.current_source_line))
        return self.visitChildren(ctx)

    def visitConst_expr(self, ctx: ASICParser.Const_exprContext):
        return self.visitChildren(ctx)

    def visitConf_c(self, ctx: ASICParser.Conf_cContext):
        const_expr_ctx = ctx.const_expr()
        if const_expr_ctx:
            const_index = const_expr_ctx.expression()[0].getText()
            shift_value = None
            if const_expr_ctx.LSHIFT():
                shift_value = int(const_expr_ctx.expression()[1].getText())
            self.config_code[-1].set_constant(int(const_index), shift_value)

        return

    def visitConf_d(self, ctx: ASICParser.Conf_dContext):
        shift_value = None
        significant_count = 32

        # Получаем название входа: v1, v1h, v2, v3, v4, r0, rev(r0)
        if ctx.vreg():
            input_name = ctx.vreg().getText()
        elif ctx.vreg_r():
            input_name = ctx.vreg_r().R0().getText()
            significant_count = 64
        else:
            raise Exception("Unknown vreg")

        # Если вход - rev(r0), то устанавливается соответствующий флаг
        if ctx.vreg_r() and ctx.vreg_r().REV():
            self.config_code[-1][120] = '1'

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
        self.config_code[-1].set_input(input_name, shift_value, significant_count)
        return

    def visitRev_configuration(self, ctx: ASICParser.Rev_configurationContext):
        self.config_code[-1][121] = '1'
        return self.visitChildren(ctx)

    def visitForloop(self, ctx: ASICParser.ForloopContext):
        # TODO: Реализовать
        return

    def is_wait_next(self, index: int) -> bool:
        if len(self.machine_code) > index + 1:
            return False
        return self.machine_code[index].is_wait()

    def insert_wait_instructions(self):
        def make_wait_instruction(cycles: int, source_line: int) -> BitInstruction:
            new_instruction = BitInstruction(source_line=source_line)
            new_instruction.set_wait(cycles)
            return new_instruction

        result = []
        last_active_index = -1

        for i, instruction in enumerate(self.machine_code):
            result.append(instruction)

            if instruction.is_start_gen():
                if self.is_wait_next(i):
                    self.machine_code[i].set_wait(max(self.machine_code[i].get_wait(), 4))
                else:
                    result.append(make_wait_instruction(4, instruction.get_source_line()))
                continue

            if instruction.is_wrout():
                if self.is_wait_next(i):
                    self.machine_code[i].set_wait(max(self.machine_code[i].get_wait(), 5))
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
