from generated.ASICParserVisitor import ASICParserVisitor
from generated.ASICParser import ASICParser
from models.Label import Label


class FirstPassVisitor(ASICParserVisitor):
    def __init__(self):
        self.labels: dict[str, Label] = {}       # Словарь для хранения меток и их адресов
        self.configs = {}      # Словарь для хранения конфигураций и их индексов
        self.defines = {}      # Словарь для хранения макросов
        self.source_line = 0   # Текущая строка
        self.config_index = 0  # Текущий индекс конфигурации

    def visitLbl(self, ctx: ASICParser.LblContext):
        # Сохранение метки с текущим адресом
        label_name = ctx.label().getText()
        self.labels[label_name] = Label(label_name, self.source_line)
        return self.visitChildren(ctx)

    def visitConfig_def(self, ctx: ASICParser.Config_defContext):
        config_name = ctx.config_name().getText()
        self.configs[config_name] = self.config_index
        self.config_index += 1
        return self.visitChildren(ctx)

    def visitDefine_def(self, ctx: ASICParser.Define_defContext):
        define_name = ctx.define_name().getText()
        self.defines[define_name] = ctx.expression().getText()
        return self.visitChildren(ctx)

    def visitLine(self, ctx: ASICParser.LineContext):
        self.source_line += 1
        return self.visitChildren(ctx)

    def get_labels(self) -> dict[str, Label]:
        return self.labels

    def get_configs(self) -> dict[str, int]:
        return self.configs

    def get_defines(self) -> dict[str, str]:
        return self.defines
