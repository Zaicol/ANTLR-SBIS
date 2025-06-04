class BitInstruction:
    def __init__(self):
        self.len = 32
        self.bits = ['0'] * self.len  # 32 бита, индекс от 0 до 31 (бит 0 — самый младший)

    def __setitem__(self, key, value):
        if isinstance(key, int):
            # Установка одного бита: obj[5] = '1'
            if not isinstance(value, str) or len(value) != 1:
                raise ValueError("Value must be a single character '0' or '1'")
            if key < 0 or key > self.len - 1:
                raise IndexError(f"Bit index out of range (0..{self.len - 1})")
            self.bits[self.len - 1 - key] = value

        elif isinstance(key, slice):
            # Обработка среза, например: obj[29:28] = '01'
            start, stop, step = key.indices(self.len)

            indices = list(range(start, stop - 1, -1)) if start >= stop else list(range(start, stop + 1))
            if len(indices) != len(value):
                raise ValueError(f"Length of value '{value}' does not match slice length {len(indices)}")

            for i, bit_index in enumerate(indices):
                if bit_index < 0 or bit_index > self.len - 1:
                    raise IndexError(f"Bit index out of range (0..{self.len - 1})")
                self.bits[self.len - 1 - bit_index] = value[i]

        else:
            raise TypeError("Index must be an integer or slice")

    def __getitem__(self, key):
        if isinstance(key, int):
            # Чтение одного бита: obj[5]
            if key < 0 or key > self.len - 1:
                raise IndexError(f"Bit index out of range (0..{self.len - 1})")
            return self.bits[self.len - 1 - key]

        elif isinstance(key, slice):
            # Чтение диапазона битов: obj[29:28]
            start, stop, step = key.indices(self.len)
            if step is not None and step != -1:
                raise ValueError("Only reverse slicing supported (e.g., [29:28])")

            indices = list(range(start, stop - 1, -1)) if start >= stop else list(range(start, stop + 1))
            return ''.join(self.bits[self.len - 1 - idx] for idx in indices)

        else:
            raise TypeError("Index must be an integer or slice")

    def __str__(self):
        return ''.join(self.bits)

    def __repr__(self):
        return f"BitInstruction({''.join(self.bits)})"

    def to_hex_list(self, prefix=False):
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
            bit_part = self.bits[i:i + 32]
            for j in range(0, 32, 4):
                nibble = ''.join(bit_part[j:j + 4])
                hex_str += hex_map.get(nibble, '?')

            hex_list.append(hex_str)

        return hex_list[::-1]

    def to_hex(self, prefix=False):
        """
        Converts the 32-bit instruction to a hexadecimal string.

        Args:
            prefix (bool): If True, adds '0x' prefix. Default is True.

        Returns:
            str: Hexadecimal representation of the instruction (uppercase).
        """
        return ("0x" if prefix else "") + ''.join(self.to_hex_list())

    def get_significant_bits(self) -> list[int]:
        indices = []
        for i, bit in enumerate(self.bits):
            if bit == '1':
                indices.append(self.len - 1 - i)
        return indices


class BitConfig(BitInstruction):
    def __init__(self, bits: str = None):
        super().__init__()
        self.len = 128
        self.bits = ['0'] * self.len
        if bits is not None:
            if len(bits) != self.len:
                raise ValueError(f"Invalid bit string length. Expected {self.len}, got {len(bits)}")
            self.bits = list(bits)
        self.constant_index = 0
        self.free_spaces = [1, 2, 3, 4]

    def to_hex(self, prefix=True):
        sup = super().to_hex_list()

        result = ""
        for i in range(4):
            result += sup[i * 8:(i + 1) * 8]

        return result

    def set_constant(self, value: int, shift_value: int = None):
        formatted_value = format(value, '07b')
        match self.constant_index:
            case 0:
                self[22:16] = formatted_value
                if shift_value is not None:
                    self[103:96] = format(shift_value, '08b')
            case 1:
                self[30:24] = formatted_value
                if shift_value is not None:
                    self[111:104] = format(shift_value, '08b')
            case 2:
                if shift_value is not None:
                    self[119:112] = format(shift_value, '08b')

        self.constant_index = self.constant_index + 1

    def set_a_input(self, space: int, reg_number: int, shift_value: int = None, significant_count: int = None):
        match space:
            case 1:
                index_regn_a, index_regn_b = 1, 0
                index_sign_a, index_sign_b = 39, 32
                index_shft_a, index_shft_b = 71, 64
            case 2:
                index_regn_a, index_regn_b = 3, 2
                index_sign_a, index_sign_b = 47, 40
                index_shft_a, index_shft_b = 79, 72
            case 3:
                index_regn_a, index_regn_b = 5, 4
                index_sign_a, index_sign_b = 55, 48
                index_shft_a, index_shft_b = 87, 80
            case 4:
                index_regn_a, index_regn_b = 7, 6
                index_sign_a, index_sign_b = 59, 52
                index_shft_a, index_shft_b = 91, 84
            case _:
                raise ValueError(f"Invalid space: {space}")

        self[index_regn_a:index_regn_b] = format(reg_number, '02b')
        if significant_count is not None:
            self[index_sign_a:index_sign_b] = format(significant_count, '08b')
        if shift_value is not None:
            self[index_shft_a:index_shft_b] = format(shift_value, '08b')

    def set_input(self, reg_name: str, shift_value: int = None, significant_count: int = 32):
        fit_space = []
        match reg_name:
            case "v1":
                fit_space = [1, 2, 4]
            case "v1h":
                fit_space = [3]
            case "v2":
                fit_space = [1, 2, 3, 4]
            case "v3":
                fit_space = [1, 2, 3, 4]
            case "v4":
                fit_space = [1, 2, 3]
            case "r0":
                fit_space = [4]

        found_space = set(self.free_spaces).intersection(fit_space)
        if len(found_space) == 0:
            raise ValueError(f"No free space for input {reg_name}")
        chosen_space = list(found_space)[0]
        self.free_spaces.remove(chosen_space)
        self.set_a_input(chosen_space, 0, shift_value, significant_count)
