from ASICParserVisitor import ASICParserVisitor
from ASICParser import ASICParser
from BitInstruction import BitInstruction, BitConfig


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


class CodeGenerator(ASICParserVisitor):
    def __init__(self, labels, configs):
        self.labels = labels          # Метки и их адреса
        self.configs = configs        # Конфигурации и их индексы
        self.machine_code: list[BitInstruction] = []        # Байтовый код программы
        self.config_code: list[BitConfig] = []

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

    def visitSregop(self, ctx:ASICParser.SregopContext):
        self.machine_code[-1][24] = '0'
        return self.visitChildren(ctx)

    def visitAluSpOp(self, ctx: ASICParser.AluSpOpContext):
        self.machine_code[-1][24] = '1'
        return self.visitChildren(ctx)

    def visitSpCopOp(self, ctx: ASICParser.SpCopOpContext):
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
            self.machine_code[-1][0] = '1'
        elif ctx_text == 'wait':
            self.machine_code[-1][27] = '1'
        elif ctx_text == 'jnz':
            self.machine_code[-1][26:25] = '11'
        return self.visitChildren(ctx)

    def visitLabel(self, ctx: ASICParser.LabelContext):
        self.machine_code[-1][7:0] = format(self.labels[ctx.getText()], '08b')
        return self.visitChildren(ctx)

    def visitConstant(self, ctx: ASICParser.ConstantContext):
        self.machine_code[-1][7:0] = format(int(ctx.getText()), '08b')

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
        if ctx_text == 'cmp':
            self.machine_code[-1][2] = '1'
            self.machine_code[-1][3] = '1'
        return self.visitChildren(ctx)

    def visitStdop(self, ctx: ASICParser.StdopContext):
        ctx_text = ctx.start.text
        self.machine_code[-1][14:12] = format(stdop_match(ctx_text), '03b')
        return self.visitChildren(ctx)

    def visitConfig_name(self, ctx: ASICParser.Config_nameContext):
        if not isinstance(ctx.parentCtx, ASICParser.Config_defContext):
            self.machine_code[-1][9:4] = format(self.configs[ctx.getText()], '06b')
        return self.visitChildren(ctx)

    def visitInstruction(self, ctx: ASICParser.InstructionContext):
        self.machine_code.append(BitInstruction())
        return self.visitChildren(ctx)

    def visitDefinition(self, ctx: ASICParser.DefinitionContext):
        self.config_code.append(BitConfig())
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
            vreg_name = ctx.vreg().getText()
        elif ctx.vreg_r():
            vreg_name = ctx.vreg_r().R0().getText()
            significant_count = 64
        else:
            raise Exception("Unknown vreg")

        if ctx.vreg_r() and ctx.vreg_r().REV():
            self.config_code[-1][120] = '1'

        if len(ctx.expression()) == 2:
            significant_count = int(ctx.expression()[0].getText())
            shift_value = int(ctx.expression()[1].getText())
        elif ctx.LSHIFT():
            shift_value = int(ctx.expression()[0].getText())
        elif len(ctx.expression()) > 0:
            significant_count = int(ctx.expression()[0].getText())

        self.config_code[-1].set_input(vreg_name, shift_value, significant_count)
        return

    def visitRev_configuration(self, ctx: ASICParser.Rev_configurationContext):
        self.config_code[-1][121] = '1'
        return self.visitChildren(ctx)

    def get_machine_code(self):
        return self.machine_code

    def get_config_code(self):
        return self.config_code

    def get_full_code(self, prefix=False) -> list[str]:
        result = [f"#conf {len(self.config_code)}"]
        prefix_str = "0x" if prefix else ""
        for config in self.config_code:
            conf_hex = config.to_hex_list(False)
            result += [prefix_str + conf_hex[i] for i in range(4)]

        result += [f"#prog {len(self.machine_code)}"]
        for instruction in self.machine_code:
            inst_hex = instruction.to_hex(False)
            result += [prefix_str + inst_hex]
        return result

    def get_full_code_str(self, prefix=False) -> str:
        code = self.get_full_code(prefix)
        return "\n".join(code)
