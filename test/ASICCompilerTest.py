import unittest
import os
import sys

from ASICAssembler import ASICAssembler
from models.exceptions.AssemblerSyntaxError import AssemblerSyntaxError
from models.exceptions.BitValueError import BitValueError
from models.exceptions.AssemblerUndefinedError import AssemblerUndefinedError


class ASICCompilerTest(unittest.TestCase):

    test_dir = "test_files"
    test_data_dir = "assembler_data"
    expected_data_dir = "expected_data"

    def assemble_code(self, filename) -> ASICAssembler:
        filepath = os.path.join(self.test_dir, self.test_data_dir, filename)

        if not os.path.exists(filepath):
            self.fail(f"Файл не найден: {filepath}")

        assembler: ASICAssembler = ASICAssembler(filepath)
        assembler.assemble()

        return assembler

    def get_expected_data(self, filename):
        filepath = os.path.join(self.test_dir, self.expected_data_dir, filename)

        if not os.path.exists(filepath):
            self.fail(f"Файл не найден: {filepath}")

        with open(filepath, "r") as f:
            return f.read()

    def test_empty_program(self):
        """Тест пустой программы"""
        filename = "test_empty.txt"
        assembler = self.assemble_code(filename)

        self.assertFalse(assembler.has_errors, "Найдены синтаксические ошибки")
        self.assertEqual(len(assembler.labels), 0, "Найдены метки")
        self.assertEqual(len(assembler.configs), 0, "Найдены конфигурации")

        hex_code = assembler.code_generator.get_full_code_hex_str()
        self.assertIsNotNone(hex_code)
        self.assertEqual(hex_code, self.get_expected_data(filename), "Код программы не совпадает")

    def test_simple_instructions(self):
        """Простой тест без меток и циклов"""
        filename = "test_simple_instructions.txt"
        assembler = self.assemble_code(filename)

        self.assertFalse(assembler.has_errors)
        self.assertEqual(len(assembler.labels), 0, "Найдены метки")

        hex_code = assembler.code_generator.get_full_code_hex_str()
        binary_code = assembler.code_generator.get_full_code_binary_str()
        print(binary_code)

        self.assertIsNotNone(hex_code)
        self.assertIsNotNone(binary_code)

        lines = [line for line in hex_code.split('\n') if line.strip() and not line.startswith('#')]
        self.assertGreater(len(lines), 0, "Код программы пустой")

        self.assertEqual(hex_code, self.get_expected_data(filename), "Код программы не совпадает")

    def test_labels(self):
        """Тест меток"""
        filename = "test_labels.txt"
        assembler = self.assemble_code(filename)
        labels = assembler.labels

        self.assertFalse(assembler.has_errors)
        self.assertEqual(len(labels), 2, "Получено не 2 метки")
        self.assertIn('l0', labels, "Должна присутствовать метка l0")
        self.assertIn('l1', labels, "Должна присутствовать метка l1")

        if 'l0' in labels and 'l1' in labels:
            self.assertNotEqual(labels['l0'], labels['l1'],
                                "Метки l0 и l1 имеют одинаковый адрес")

        hex_code = assembler.code_generator.get_full_code_hex_str()
        self.assertEqual(hex_code, self.get_expected_data(filename), "Код программы не совпадает")

    def test_configs(self):
        """Тест конфигураций"""
        filename = "test_configs.txt"
        assembler = self.assemble_code(filename)
        configs = assembler.configs

        self.assertFalse(assembler.has_errors)
        self.assertEqual(len(configs), 2, "Получено не 2 конфигурации")
        self.assertIn('conf_0', configs, "Должна присутствовать конфигурация conf_0")
        self.assertIn('conf_1', configs, "Должна присутствовать конфигурация conf_1")
        config_indices = list(configs.values())
        self.assertEqual(len(config_indices), len(set(config_indices)),
                         f"Конфигурации имеют одинаковый индекс: {config_indices}")

        hex_code = assembler.code_generator.get_full_code_hex_str()
        self.assertIn("#conf", hex_code, "В программе нет конфигураций")
        self.assertEqual(hex_code, self.get_expected_data(filename), "Код программы не совпадает")

    def test_wait(self):
        """Тест различных значений wait"""
        filename = "test_wait.txt"
        assembler = self.assemble_code(filename)

        hex_code = assembler.code_generator.get_full_code_hex_str()
        self.assertEqual(hex_code, self.get_expected_data(filename), "Код программы не совпадает")

    def test_hex_and_binary_consistency(self):
        """Тест согласованности hex и binary представлений"""
        filename = "test_consistency.txt"
        assembler = self.assemble_code(filename)
        code_gen = assembler.code_generator

        hex_code = code_gen.get_full_code_hex_str(show_source_line=True)
        binary_code = code_gen.get_full_code_binary_str(show_source_line=True)

        hex_lines = [line for line in hex_code.split('\n')
                     if ':' in line and not line.strip().startswith('#')]
        binary_lines = [line for line in binary_code.split('\n')
                        if ':' in line and not line.strip().startswith('#')]

        self.assertEqual(len(hex_lines), len(binary_lines),
                         "Количество инструкций в hex и binary не совпадает")

        for hex_line, bin_line in zip(hex_lines, binary_lines):
            hex_line_num = hex_line.split(':')[0].strip()
            bin_line_num = bin_line.split(':')[0].strip()
            self.assertEqual(hex_line_num, bin_line_num,
                             f"Не совпадают номера строк: {hex_line_num} и {bin_line_num}")

            hex_value = hex_line.split(':')[1].strip()
            bin_value = bin_line.split(':')[1].strip().replace('_', '')

            dec_from_hex = int(hex_value, 16)
            dec_from_bin = int(bin_value, 2)

            self.assertEqual(dec_from_hex, dec_from_bin,
                             f"Строки с номером {hex_line_num} различаются")

    def test_no_syntax_errors(self):
        """Тест, что все валидные файлы не содержат синтаксических ошибок"""
        test_files = [
            "test_empty.txt",
            "test_simple_instructions.txt",
            "test_labels.txt",
            "test_configs.txt",
            "test_wait.txt",
            "test_consistency.txt"
        ]

        for filename in test_files:
            with self.subTest(file=filename):
                assembler = self.assemble_code(filename)
                self.assertFalse(assembler.has_errors,
                                 f"Файл {filename} содержит синтаксические ошибки")

    def test_has_syntax_errors(self):
        """Тест на определение ошибок"""
        test_dir = "syntax_errors"
        test_cases = [
            ("test_error_unknown_operator.txt", AssemblerSyntaxError,
             "Syntax error: no viable alternative at input 'r1!='"),
            ("test_error_no_config.txt", AssemblerUndefinedError,
             "Undefined identifier: 'conf_1'"),
            ("test_error_constant.txt", BitValueError,
             "Expression value 16777217 out of range [0, 16777215]"),
        ]

        for filename, expected_exception, expected_message in test_cases:
            with self.subTest(file=filename, error=expected_exception.__name__):
                filepath = os.path.join(test_dir, filename)

                with self.assertRaises(expected_exception) as ex:
                    self.assemble_code(filepath)
                self.assertEqual(str(ex.exception.message), expected_message)


def run_tests():
    """Запуск всех тестов"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(ASICCompilerTest)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())
