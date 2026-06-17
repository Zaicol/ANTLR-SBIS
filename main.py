import sys
from antlr4 import *
from generated.ASICLexer import ASICLexer
from generated.ASICParser import ASICParser
from models.exceptions.AssemblerErrorListener import AssemblerErrorListener
from visitors.CodeGenerator import CodeGenerator
from visitors.LabelCollector import LabelCollector
from utils.tree import generate_graph_tree


TEST_FILE_NAME = "test_files/test1.txt"
SHOW_SOURCE_LINES = True
ADD_PREFIX = False


def main():
    # Создание потока входных данных
    input_stream = FileStream(TEST_FILE_NAME, encoding="utf-8")

    # Создаем лексер и парсер
    lexer = ASICLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ASICParser(token_stream)

    parser.removeErrorListeners()
    error_listener = AssemblerErrorListener()
    parser.addErrorListener(error_listener)

    # Парсим программу и создаем дерево разбора
    tree = parser.prog()
    print("Дерево разбора создано")
    # print(tree.toStringTree(recog=parser))
    generate_graph_tree(tree, parser)

    # Проверка на наличие ошибок
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors found in the code.")
    else:
        print("No syntax errors found.")

    print(tree.toStringTree(recog=parser))
    print_break()

    # Первый проход: сбор меток
    label_collector = LabelCollector()
    label_collector.visit(tree)
    labels = label_collector.get_labels()
    configs = label_collector.get_configs()
    defines = label_collector.get_defines()
    print("Найденные метки и их адреса:", labels)
    print("Найденные конфигурации и их индексы:", configs)
    print("Найденные макросы:", defines)

    print_break()

    # Второй проход: генерация машинного кода
    code_generator = CodeGenerator(labels, configs, defines)
    code_generator.visit(tree)
    code_generator.insert_wait_instructions()
    print_code(code_generator)


def print_break():
    break_line = "=" * 30
    print(f"\n{break_line}\n")


def print_code(code_generator: CodeGenerator):
    print("Сгенерированный машинный код (hex):")
    print(code_generator.get_full_code_hex_str(prefix=ADD_PREFIX,
                                               show_source_line=SHOW_SOURCE_LINES,
                                               split_bytes=True))

    print_break()

    print("Сгенерированный машинный код (binary):")
    print(code_generator.get_full_code_binary_str(show_source_line=SHOW_SOURCE_LINES))


if __name__ == '__main__':
    main()
