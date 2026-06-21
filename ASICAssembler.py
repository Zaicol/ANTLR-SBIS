from antlr4 import *
from antlr4.tree.Tree import ParseTree

from generated.ASICLexer import ASICLexer
from generated.ASICParser import ASICParser
from models.Label import Label
from models.exceptions.AssemblerErrorListener import AssemblerErrorListener
from visitors.CodeGenerator import CodeGenerator
from visitors.FirstPassVisitor import FirstPassVisitor
from utils.tree import generate_graph_tree


class ASICAssembler:
    def __init__(self, source_file: str):
        self.source_file = source_file
        self.tree = None
        self.parser = None
        self.labels: dict[str, Label] = {}
        self.configs: dict[str, int] = {}
        self.defines: dict[str, ASICParser.ExpressionContext] = {}
        self.constant_contexts: dict[str, ASICParser.Const_exprContext] = {}
        self.code_generator = None

    def parse(self) -> ParseTree:
        """Первый этап: лексический и синтаксический анализ"""
        input_stream = FileStream(self.source_file, encoding="utf-8")
        lexer = ASICLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        self.parser = ASICParser(token_stream)

        # Настройка обработчика ошибок
        self.parser.removeErrorListeners()
        error_listener = AssemblerErrorListener()
        self.parser.addErrorListener(error_listener)

        # Парсинг
        self.tree = self.parser.prog()

        if self.has_errors:
            print("Syntax errors found in the code.")
        else:
            print("No syntax errors found.")

        return self.tree

    def first_pass(self) -> FirstPassVisitor:
        """Второй этап: сбор меток, конфигураций и макросов"""
        label_collector = FirstPassVisitor()
        label_collector.visit(self.tree)

        self.labels = label_collector.get_labels()
        self.configs = label_collector.get_configs()
        self.defines = label_collector.get_defines()
        self.constant_contexts = label_collector.get_constant_contexts()

        return label_collector

    def generate_code(self) -> list:
        """Третий этап: генерация машинного кода"""
        self.code_generator = CodeGenerator(
            self.labels,
            self.configs,
            self.defines,
            self.constant_contexts
        )
        self.code_generator.visit(self.tree)
        self.code_generator.insert_wait_instructions()

        return self.code_generator.get_machine_code()

    def assemble(self) -> list:
        """Полный процесс сборки"""
        self.parse()
        self.first_pass()
        return self.generate_code()

    @property
    def has_errors(self) -> bool:
        """Проверка наличия синтаксических ошибок"""
        if self.parser is None:
            return False
        return self.parser.getNumberOfSyntaxErrors() > 0
