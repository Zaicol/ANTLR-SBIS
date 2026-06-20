from ASICCompiler import ASICCompiler
from visitors.CodeGenerator import CodeGenerator
from utils.tree import generate_graph_tree


TEST_FILE_NAME = "test/test_files/test1.txt"
SHOW_SOURCE_LINES = True
ADD_PREFIX = False


def main():
    # Создание потока входных данных
    compiler: ASICCompiler = ASICCompiler(TEST_FILE_NAME)
    compiler.assemble()

    tree = compiler.tree
    parser = compiler.parser
    generate_graph_tree(tree, parser)

    print(tree.toStringTree(recog=parser))
    print_break()

    print("Найденные метки и их адреса:", compiler.labels)
    print("Найденные конфигурации и их индексы:", compiler.configs)
    print("Найденные макросы:", compiler.defines)

    print_break()

    print_code(compiler.code_generator)


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
