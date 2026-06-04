class BitInstruction:
    # TODO: Вынести всё в константы
    # TODO: Переписать с использованием int
    def __init__(self):
        self.len: int = 32
        self.bits: list[str] = ['0'] * self.len  # 32 бита, индекс от 0 до 31 (бит 0 — самый младший)

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

    def to_binary_list(self) -> list[str]:

        # Split into groups of 4 bits from left to right (MSB to LSB)
        bin_list = []
        for i in range(0, self.len, 32):
            tmp_list = []
            for j in range(8):
                tmp_list.append(''.join(self.bits[i + j * 4:i + j * 4 + 4]))
            bin_list.append('_'.join(tmp_list))

        return bin_list[::-1]

    def get_significant_bits(self) -> list[int]:
        indices = []
        for i, bit in enumerate(self.bits):
            if bit == '1':
                indices.append(self.len - 1 - i)
        return indices

    def set_wait(self, cycles: int):
        self[27] = '1'
        self[7:0] = format(cycles, '08b')

    # ===================== BOOLEAN МЕТОДЫ =====================
    # === БАЗОВЫЕ ПРИЗНАКИ ===

    def is_standard(self) -> bool:
        return self[24] == '1'

    def is_service(self) -> bool:
        return self[24] == '0'

    def is_active(self) -> bool:
        return self[2] == '1'

    def is_passive(self) -> bool:
        return self[2] == '0'

    def is_wait(self) -> bool:
        return self[27] == '1'

    def is_eop(self) -> bool:
        return self[31] == '1'

    # === ОПЕРАЦИИ С ДАННЫМИ ===

    def is_start_gen(self) -> bool:
        return self[0] == '1'

    def is_wrout(self) -> bool:
        return self[1] == '1'

    def is_read(self) -> bool:
        return self[2] == '1'

    def uses_wbuf_mask(self) -> bool:
        return any(self[i] == '1' for i in range(16, 20))

    def uses_xor_write(self) -> bool:
        return self[20] == '1'

    def uses_and_write(self) -> bool:
        return self[21] == '1'

    # ===================== РАБОТА С БЛОКАМИ =====================

    def is_alu(self) -> bool:
        return self[15] == '1'

    def is_sp(self) -> bool:
        return self[15] == '0'

    def get_active_block(self) -> int:
        return (
                (int(self[12]) << 0) |
                (int(self[13]) << 1) |
                (int(self[14]) << 2)
        )

    # === СЛУЖЕБНЫЕ ИНСТРУКЦИИ ===

    def get_type1(self) -> int:
        return (
                (int(self[25]) << 0) |
                (int(self[26]) << 1)
        )

    def is_init(self) -> bool:
        return self.is_service() and self.get_type1() == 0

    def is_inc_dec(self) -> bool:
        return self.is_service() and self.get_type1() == 1

    def is_assign(self) -> bool:
        return self.is_service() and self.get_type1() == 2

    def is_jump(self) -> bool:
        return self.is_service() and self.get_type1() == 3

    # === РЕГИСТРЫ ===

    def get_reg(self) -> int:
        return (int(self[28]) << 0) | (int(self[29]) << 1)

    def is_inc(self) -> bool:
        return self.is_inc_dec() and self[30] == '1'

    def is_dec(self) -> bool:
        return self.is_inc_dec() and self[30] == '0'

    # === СОСТАВНЫЕ ПРИЗНАКИ ДЛЯ WAIT ===

    def is_active_standard(self) -> bool:
        return self.is_standard() and self.is_active()

    def is_passive_standard(self) -> bool:
        return self.is_standard() and self.is_passive()

    def is_long_latency_op(self) -> bool:
        return self.is_active_standard()

    def requires_gen_wait(self) -> bool:
        return self.is_start_gen()

    def requires_wrout_wait(self) -> bool:
        return self.is_wrout()

    def modifies_register(self) -> bool:
        return self.is_init() or self.is_inc_dec() or self.is_assign()

    def is_data_dependent_candidate(self) -> bool:
        return (
                self.is_active_standard()
                or self.is_wrout()
                or self.is_start_gen()
        )

    def get_wait(self):
        if not self.is_wait():
            return 0
        return (
                (int(self[0]) << 0) |
                (int(self[1]) << 1) |
                (int(self[2]) << 2) |
                (int(self[3]) << 3) |
                (int(self[4]) << 4) |
                (int(self[5]) << 5) |
                (int(self[6]) << 6) |
                (int(self[7]) << 7)
        )
