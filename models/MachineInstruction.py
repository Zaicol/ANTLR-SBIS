from enum import IntEnum


class MachineInstruction:
    """
    Класс для представления инструкции в виде списка битов
    """
    len: int = 32

    def __init__(self, source_line: int = 0):
        self.source_line = source_line
        self.bits: list[int] = [0 for _ in range(self.len)]

    def __setitem__(self, key: int | slice, value: int | IntEnum | bool):

        if isinstance(value, bool):
            value = 1 if value else 0

        if isinstance(value, IntEnum):
            value = value.value

        if not isinstance(value, int):
            raise TypeError(f"Bit value expected to be an integer, but got {type(value)}")

        if isinstance(key, int):
            # Установка одного бита: obj[5] = 1
            if not isinstance(value, int) or value not in [0, 1]:
                raise ValueError("Value must be a single number 0 or 1")
            if key < 0 or key > self.len - 1:
                raise IndexError(f"Bit index out of range [0..{self.len - 1}]")
            bit_idx: int = self.len - 1 - key
            self.bits[bit_idx] = value

        elif isinstance(key, slice):
            # Обработка среза, например: obj[29:28] = 01
            start, stop, step = key.indices(self.len)

            # Поддержка и прямого, и обратного среза (например, [29:28] и [28:29])
            indices = list(range(start, stop - 1, -1)) if start >= stop else list(range(start, stop + 1))

            # Преобразуем число в битовую строку с нужной длиной
            bit_length = len(indices)
            value_str = format(value, f'0{bit_length}b')  # например: format(5, '04b') -> '0101'

            if len(value_str) != bit_length:
                # Значение слишком большое
                raise ValueError(f"Value {value} (0b{value:b}) requires more than {bit_length} bits")

            for i, bit_index in enumerate(indices):
                if bit_index < 0 or bit_index > self.len - 1:
                    raise IndexError(f"Bit index out of range (0..{self.len - 1})")
                bit_idx: int = self.len - 1 - bit_index
                self.bits[bit_idx] = int(value_str[i])

        else:
            raise TypeError("Index must be an integer or slice")

    def __getitem__(self, key) -> int:
        if isinstance(key, int):
            # Чтение одного бита: obj[5]
            if key < 0 or key > self.len - 1:
                raise IndexError(f"Bit index out of range (0..{self.len - 1})")
            return self.bits[self.len - 1 - key]

        elif isinstance(key, slice):
            # Чтение диапазона битов: obj[29:28]
            start, stop, step = key.indices(self.len)

            indices = list(range(start, stop - 1, -1)) if start >= stop else list(range(start, stop + 1))
            bits_slice = [self.bits[self.len - 1 - idx] for idx in indices]
            return int(''.join(map(str, bits_slice)), 2)

        else:
            raise TypeError("Index must be an integer or slice")

    def __str__(self) -> str:
        return ''.join(str(self.bits))

    def __repr__(self) -> str:
        return f"BitInstruction({self.source_line}: {self.__str__()})"

    def get_str(self, key: int | slice) -> str:
        if isinstance(key, int):
            # Чтение одного бита: obj[5]
            if key < 0 or key > self.len - 1:
                raise IndexError(f"Bit index out of range (0..{self.len - 1})")
            return str(self.bits[self.len - 1 - key])

        elif isinstance(key, slice):
            # Чтение диапазона битов: obj[29:28]
            start, stop, step = key.indices(self.len)

            indices = list(range(start, stop - 1, -1)) if start >= stop else list(range(start, stop + 1))
            return ''.join(str(self.bits[self.len - 1 - idx]) for idx in indices)

        else:
            raise TypeError("Index must be an integer or slice")

    def set_source_line(self, source_line: int):
        self.source_line = source_line

    def get_source_line(self):
        return self.source_line

    def to_hex(self, prefix=False, split_bytes=False) -> list[str]:
        hex_map = {
            '0000': '0', '0001': '1', '0010': '2', '0011': '3',
            '0100': '4', '0101': '5', '0110': '6', '0111': '7',
            '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
            '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
        }

        # Split into groups of 4 bits from left to right (MSB to LSB)
        hex_list = []
        for i in range(0, self.len, 32):
            hex_str = '0x' if prefix else ''
            bit_word = self.bits[i:i + 32]
            for j in range(0, 32, 4):
                if split_bytes and j % 8 == 0 and j != 0:
                    hex_str += ' '

                nibble = ''.join(map(str, bit_word[j:j + 4]))
                hex_str += hex_map.get(nibble, '?')

            hex_list.append(hex_str)

        return hex_list[::-1]

    def to_hex_str(self, prefix=False, split_bytes=False):
        """
        Converts the 32-bit instruction to a hexadecimal string.
            :param prefix: If True, adds '0x' prefix. Default is True.
            :param split_bytes: If True, adds space between bytes. Default is False.

            :return: Hexadecimal representation of the instruction (uppercase).
        """
        hex_str = ''.join(self.to_hex(prefix, split_bytes))
        return ("0x" if prefix else "") + hex_str

    def to_binary_list(self, size=32) -> list[str]:

        # Split into groups of 4 bits from left to right (MSB to LSB)
        bin_list = []
        for i in range(0, self.len, size):
            tmp_list = []
            for j in range(8):
                tmp_list.append(''.join(map(str, self.bits[i + j * 4:i + j * 4 + 4])))
            bin_list.append('_'.join(tmp_list))

        return bin_list[::-1]

    def get_significant_bits(self) -> list[int]:
        indices = []
        for i, bit in enumerate(self.bits):
            if bit == '1':
                indices.append(self.len - 1 - i)
        return indices
