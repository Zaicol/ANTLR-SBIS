from generated.ASICParserVisitor import ASICParserVisitor
from generated.ASICParser import ASICParser


class LabelCollector(ASICParserVisitor):
    def __init__(self):
        self.labels = {}       # Словарь для хранения меток и их адресов
        self.configs = {}      # Словарь для хранения конфигураций и их индексов
        self.defines = {}      # Словарь для хранения макросов
        self.line = -1         # Текущая строка
        self.config_index = 0  # Текущий индекс конфигурации

    def visitLbl(self, ctx: ASICParser.LblContext):
        # Сохранение метки с текущим адресом
        label_name = ctx.label().getText()
        self.labels[label_name] = self.line
        return self.visitChildren(ctx)

    def visitStatement(self, ctx: ASICParser.StatementContext):
        # Увеличение адреса для каждой инструкции
        self.line += 1
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

    def get_labels(self):
        return self.labels

    def get_configs(self):
        return self.configs

    def get_defines(self):
        return self.defines
