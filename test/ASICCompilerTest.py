import unittest
import os
import sys

from ASICCompiler import ASICCompiler
from models.exceptions.AssemblerSyntaxError import AssemblerSyntaxError
from models.exceptions.BitValueError import BitValueError
from models.exceptions.SemanticError import SemanticError


class ASICCompilerTest(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_files"
        self.test_data_dir = "assembler_data"
        self.expected_data_dir = "expected_data"

    def generate_machine_code(self, filename):
        """
        Вспомогательный метод
        Возвращает: (labels, configs, code_generator, has_errors)
        """

        filepath = os.path.join(self.test_dir, self.test_data_dir, filename)

        if not os.path.exists(filepath):
            self.fail(f"Файл не найден: {filepath}")

        compiler: ASICCompiler = ASICCompiler(filepath)

        compiler.assemble()
        labels = compiler.labels
        configs = compiler.configs
        code_generator = compiler.code_generator
        has_errors = compiler.has_errors

        return labels, configs, code_generator, has_errors

    def get_expected_data(self, filename):
        filepath = os.path.join(self.test_dir, self.expected_data_dir, filename)

        if not os.path.exists(filepath):
            self.fail(f"Файл не найден: {filepath}")

        with open(filepath, "r") as f:
            return f.read()

    def test_empty_program(self):
        """Тест пустой программы"""
        filename = "test_empty.txt"
        labels, configs, code_gen, has_errors = self.generate_machine_code(filename)

        self.assertFalse(has_errors, "Найдены синтаксические ошибки")
        self.assertEqual(len(labels), 0, "Найдены метки")
        self.assertEqual(len(configs), 0, "Найдены конфигурации")

        hex_code = code_gen.get_full_code_hex_str()
        self.assertIsNotNone(hex_code)
        self.assertEqual(hex_code, self.get_expected_data(filename), "Код программы не совпадает")

    def test_simple_instructions(self):
        """Простой тест без меток и циклов"""
        filename = "test_simple_instructions.txt"
        labels, configs, code_gen, has_errors = self.generate_machine_code(filename)

        self.assertFalse(has_errors)
        self.assertEqual(len(labels), 0, "Найдены метки")

        hex_code = code_gen.get_full_code_hex_str()
        binary_code = code_gen.get_full_code_binary_str()

        self.assertIsNotNone(hex_code)
        self.assertIsNotNone(binary_code)

        lines = [line for line in hex_code.split('\n') if line.strip() and not line.startswith('#')]
        self.assertGreater(len(lines), 0, "Код программы пустой")

        self.assertEqual(hex_code, self.get_expected_data(filename), "Код программы не совпадает")

    def test_labels(self):
        """Тест меток"""
        filename = "test_labels.txt"
        labels, configs, code_gen, has_errors = self.generate_machine_code(filename)

        self.assertFalse(has_errors)
        self.assertEqual(len(labels), 2, "Получено не 2 метки")
        self.assertIn('l0', labels, "Должна присутствовать метка l0")
        self.assertIn('l1', labels, "Должна присутствовать метка l1")

        if 'l0' in labels and 'l1' in labels:
            self.assertNotEqual(labels['l0'], labels['l1'],
                                "Метки l0 и l1 имеют одинаковый адрес")

        hex_code = code_gen.get_full_code_hex_str()
        self.assertEqual(hex_code, self.get_expected_data(filename), "Код программы не совпадает")

    def test_configs(self):
        """Тест конфигураций"""
        filename = "test_configs.txt"
        labels, configs, code_gen, has_errors = self.generate_machine_code(filename)

        self.assertFalse(has_errors)
        self.assertEqual(len(configs), 3, "Получено не 3 конфигурации")
        self.assertIn('conf_0', configs, "Должна присутствовать конфигурация conf_0")
        self.assertIn('conf_1', configs, "Должна присутствовать конфигурация conf_1")
        self.assertIn('conf_2', configs, "Должна присутствовать конфигурация conf_2")

        config_indices = list(configs.values())
        self.assertEqual(len(config_indices), len(set(config_indices)),
                         f"Конфигурации имеют одинаковый индекс: {config_indices}")

        hex_code = code_gen.get_full_code_hex_str()
        self.assertIn("#conf", hex_code, "В программе нет конфигураций")
        self.assertEqual(hex_code, self.get_expected_data(filename), "Код программы не совпадает")

    def test_wait(self):
        """Тест различных значений wait"""
        filename = "test_wait.txt"
        labels, configs, code_gen, has_errors = self.generate_machine_code(filename)

        self.assertFalse(has_errors)
        hex_code = code_gen.get_full_code_hex_str()
        self.assertEqual(hex_code, self.get_expected_data(filename), "Код программы не совпадает")

    def test_hex_and_binary_consistency(self):
        """Тест согласованности hex и binary представлений"""
        filename = "test_consistency.txt"
        labels, configs, code_gen, has_errors = self.generate_machine_code(filename)

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
                _, _, _, has_errors = self.generate_machine_code(filename)
                self.assertFalse(has_errors,
                                 f"Файл {filename} содержит синтаксические ошибки")

    def test_has_syntax_errors(self):
        """Тест на определение ошибок"""
        test_dir = "syntax_errors"
        test_cases = [
            ("test_error_unknown_operator.txt", AssemblerSyntaxError),
            ("test_error_no_config.txt", SemanticError),
            ("test_error_constant.txt", BitValueError),
        ]

        for filename, expected_exception in test_cases:
            with self.subTest(file=filename, error=expected_exception.__name__):
                filepath = os.path.join(test_dir, filename)

                with self.assertRaises(expected_exception):
                    self.generate_machine_code(filepath)


def run_tests():
    """Запуск всех тестов"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(ASICCompilerTest)

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())
