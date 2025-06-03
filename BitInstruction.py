class BitInstruction:
    def __init__(self):
        self.bits = ['0'] * 32  # 32 бита, индекс от 0 до 31 (бит 0 — самый младший)

    def __setitem__(self, key, value):
        if isinstance(key, int):
            # Установка одного бита: obj[5] = '1'
            if not isinstance(value, str) or len(value) != 1:
                raise ValueError("Value must be a single character '0' or '1'")
            if key < 0 or key > 31:
                raise IndexError("Bit index out of range (0..31)")
            self.bits[31 - key] = value

        elif isinstance(key, slice):
            # Обработка среза, например: obj[29:28] = '01'
            start, stop, step = key.indices(32)

            indices = list(range(start, stop - 1, -1)) if start >= stop else list(range(start, stop + 1))
            if len(indices) != len(value):
                raise ValueError(f"Length of value '{value}' does not match slice length {len(indices)}")

            for i, bit_index in enumerate(indices):
                if bit_index < 0 or bit_index > 31:
                    raise IndexError("Bit index out of range (0..31)")
                self.bits[31 - bit_index] = value[i]

        else:
            raise TypeError("Index must be an integer or slice")

    def __getitem__(self, key):
        if isinstance(key, int):
            # Чтение одного бита: obj[5]
            if key < 0 or key > 31:
                raise IndexError("Bit index out of range (0..31)")
            return self.bits[31 - key]

        elif isinstance(key, slice):
            # Чтение диапазона битов: obj[29:28]
            start, stop, step = key.indices(32)
            if step is not None and step != -1:
                raise ValueError("Only reverse slicing supported (e.g., [29:28])")

            indices = list(range(start, stop - 1, -1)) if start >= stop else list(range(start, stop + 1))
            return ''.join(self.bits[31 - idx] for idx in indices)

        else:
            raise TypeError("Index must be an integer or slice")

    def __str__(self):
        return ''.join(self.bits)

    def __repr__(self):
        return f"BitInstruction({''.join(self.bits)})"

    def to_hex(self, prefix=True):
        """
        Converts the 32-bit instruction to a hexadecimal string.

        Args:
            prefix (bool): If True, adds '0x' prefix. Default is True.

        Returns:
            str: Hexadecimal representation of the instruction (uppercase).
        """
        hex_map = {
            '0000': '0', '0001': '1', '0010': '2', '0011': '3',
            '0100': '4', '0101': '5', '0110': '6', '0111': '7',
            '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
            '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
        }

        # Split into groups of 4 bits from left to right (MSB to LSB)
        hex_str = ''
        for i in range(0, 32, 4):
            nibble = ''.join(self.bits[i:i + 4])
            hex_str += hex_map.get(nibble, '?')

        if prefix:
            return f"0x{hex_str}"
        else:
            return hex_str
