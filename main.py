import sys
from antlr4 import *
from ASICLexer import ASICLexer
from ASICParser import ASICParser
from CodeGenerator import CodeGenerator
from LabelCollector import LabelCollector
from tree import generate_graph_tree


def main(argv):
    # Создание потока входных данных
    input_stream = FileStream("test1.txt", encoding="utf-8")

    # Создаем лексер и парсер
    lexer = ASICLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ASICParser(token_stream)

    # Парсим программу и создаем дерево разбора
    tree = parser.prog()
    print("Дерево разбора создано:", tree.toStringTree(recog=parser))
    generate_graph_tree(tree, parser)

    # Проверка на наличие ошибок
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors found in the code.")
    else:
        print("No syntax errors found.")

    print("\n==================\n")

    # Первый проход: сбор меток
    label_collector = LabelCollector()
    label_collector.visit(tree)
    labels = label_collector.get_labels()
    configs = label_collector.get_configs()
    print("Найденные метки и их адреса:", labels)
    print("Найденные конфигурации и их индексы:", configs)

    print("\n==================\n")

    # Второй проход: генерация машинного кода
    code_generator = CodeGenerator(labels, configs)
    code_generator.visit(tree)
    print("Сгенерированный машинный код:")

    print(code_generator.get_full_code_str(prefix=False))


if __name__ == '__main__':
    main(sys.argv)
