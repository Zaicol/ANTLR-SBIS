from models.BitInstruction import BitInstruction


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
                fit_space = [2, 1, 4]
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
