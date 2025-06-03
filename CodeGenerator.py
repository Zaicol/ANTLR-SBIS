from ASICParserVisitor import ASICParserVisitor
from ASICParser import ASICParser
from BitInstruction import BitInstruction


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
        if op == '--':
            self.machine_code[-1][25] = '1'
            self.machine_code[-1][30] = '0'
        elif op == '++':
            self.machine_code[-1][25] = '1'
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
        print(format(self.configs[ctx.getText()], '05b'))
        self.machine_code[-1][9:4] = format(self.configs[ctx.getText()], '06b')
        return self.visitChildren(ctx)

    def visitInstruction(self, ctx: ASICParser.InstructionContext):
        self.machine_code.append(BitInstruction())
        return self.visitChildren(ctx)

    def visitDefinition(self, ctx: ASICParser.DefinitionContext):
        return

    def get_machine_code(self):
        return self.machine_code
