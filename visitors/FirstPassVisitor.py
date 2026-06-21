from generated.ASICParserVisitor import ASICParserVisitor
from generated.ASICParser import ASICParser
from models.Label import Label
from models.exceptions.AssemblerDuplicateError import AssemblerDuplicateError
from models.exceptions.AssemblerSyntaxError import AssemblerSyntaxError


class FirstPassVisitor(ASICParserVisitor):

    RESERVED = {"v1", "v2", "v3", "v4",
                "v1h", "v2^", "v4&", "r0",
                "r1", "r2", "r3", "$0",
                "$1", "$2", "$3", "gen",
                "wait", "jnz", "eop", "a1",
                "a4", "a5", "a128d", "d",
                "dinv", "id", "and", "or",
                "xor", "not", "inv", "rev"}

    def __init__(self):
        self.labels: dict[str, Label] = {}       # Словарь для хранения меток и их адресов
        self.configs = {}      # Словарь для хранения конфигураций и их индексов
        self.defines = {}      # Словарь для хранения макросов
        self.constant_contexts: dict[str, ASICParser.Const_exprContext] = {}    # Словарь для хранения констант
        self.source_line = 0   # Текущая строка
        self.config_index = 0  # Текущий индекс конфигурации

    def visitLbl(self, ctx: ASICParser.LblContext):
        # Сохранение метки с текущим адресом
        label_name = ctx.label().getText()
        self.check_reserved(label_name)
        if label_name in self.labels:
            raise AssemblerDuplicateError(label_name, line=self.source_line)

        self.labels[label_name] = Label(label_name, self.source_line)
        return self.visitChildren(ctx)

    def visitConfig_def(self, ctx: ASICParser.Config_defContext):
        config_name = ctx.config_name().getText()
        self.check_reserved(config_name)
        if config_name in self.configs:
            raise AssemblerDuplicateError(config_name, line=self.source_line)

        self.configs[config_name] = self.config_index
        self.config_index += 1
        return self.visitChildren(ctx)

    def visitDefine_def(self, ctx: ASICParser.Define_defContext):
        define_name = ctx.define_name().getText()
        self.check_reserved(define_name)
        if define_name in self.defines:
            raise AssemblerDuplicateError(define_name, line=self.source_line)

        self.defines[define_name] = ctx.expression().getText()
        return self.visitChildren(ctx)

    def visitConst_def(self, ctx:ASICParser.Const_defContext):
        const_name = ctx.const_name().getText()
        self.check_reserved(const_name)
        if const_name in self.constant_contexts:
            raise AssemblerDuplicateError(const_name, line=self.source_line)

        self.constant_contexts[const_name] = ctx.const_expr()
        return self.visitChildren(ctx)

    def visitLine(self, ctx: ASICParser.LineContext):
        self.source_line += 1
        return self.visitChildren(ctx)

    def check_reserved(self, name: str):
        if name in self.RESERVED:
            raise AssemblerSyntaxError(f"Can't use reserved name '{name}'!", self.source_line)

    def get_labels(self) -> dict[str, Label]:
        return self.labels

    def get_configs(self) -> dict[str, int]:
        return self.configs

    def get_defines(self) -> dict[str, str]:
        return self.defines

    def get_constant_contexts(self) -> dict[str, ASICParser.Const_exprContext]:
        return self.constant_contexts
