from models.BitInstruction import BitInstruction
from models.Constant import Constant
from models.enums.ConfigEnums import InputName


class BitConfig(BitInstruction):
    # Адреса аргументов
    # Аргументы для MUX
    A1 = slice(1, 0, -1)
    A2 = slice(3, 2, -1)
    A3 = slice(5, 4, -1)
    A4 = slice(7, 6, -1)

    REC3 = 8  # признак чтения из БПК2
    AC = slice(11, 10, -1)  # способ формирования адреса чтения константы const3 из БПК2
    ARR = slice(13, 12, -1)  # номер регистра, адресующего порт чтения БПК
    DIR = 14  # признак использования регистра или прямого адреса arc1

    # Адреса констант в БПК
    ARC1 = slice(22, 16, -1)
    ARC2 = slice(30, 24, -1)

    # Аргументы для TRUNC
    TR_R1 = slice(39, 32, -1)
    TR_R2 = slice(47, 40, -1)
    TR_R3 = slice(55, 48, -1)
    TR_R4 = slice(63, 56, -1)

    # Аргументы для SHIFT
    SH_R1 = slice(71, 64, -1)
    SH_R2 = slice(79, 72, -1)
    SH_R3 = slice(87, 80, -1)
    SH_R4 = slice(95, 88, -1)

    SH_C1 = slice(103, 96, -1)
    SH_C2 = slice(111, 104, -1)
    SH_C3 = slice(119, 112, -1)

    # Аргументы для REV
    REV_REG = 120
    REV_TXT = 121

    def __init__(self, bits: str = None, source_line: int = 0):
        super().__init__()
        self.len = 128
        self.bits = [0 for _ in range(self.len)]
        if bits is not None:
            if len(bits) != self.len:
                raise ValueError(f"Invalid bit string length. Expected {self.len}, got {len(bits)}")
            self.bits = list(bits)
        self.constant_index = 0
        self.is_const3_set = False
        self.free_spaces = [1, 2, 3, 4]
        self.source_line = source_line

    def to_hex_str(self, prefix=True, split_bytes=False):
        sup = super().to_hex()

        result = ""
        for i in range(4):
            result += sup[i * 8:(i + 1) * 8]

        return result

    def set_const3(self, constant: Constant):
        if self.is_const3_set:
            raise ValueError("Constant 3 is already set")

        bpd = constant.get_bpd()
        shift_value = constant.get_shift()
        if bpd is not None:
            self[self.REC3] = True
            self[self.AC] = bpd
        if shift_value is not None:
            self[self.SH_C3] = shift_value

        self.is_const3_set = True

    def set_const1(self, constant: Constant):
        reg = constant.get_reg()
        address = constant.get_address()
        shift_value = constant.get_shift()
        if reg is not None:
            self[self.DIR] = True
            self[self.ARR] = reg
        else:
            self[self.ARC1] = address
        if shift_value is not None:
            self[self.SH_C1] = shift_value

    def set_const2(self, constant: Constant):
        reg = constant.get_reg()
        address = constant.get_address()
        shift_value = constant.get_shift()

        if reg is not None:
            if self[self.DIR]:
                raise ValueError("const1 is already set")
            else:
                self[self.DIR] = True
                self[self.ARR] = reg

                self[self.ARC2] = self[self.ARC1]
                self[self.SH_C2] = self[self.SH_C1]

                self.set_const1(constant)
            return

        self[self.ARC2] = address
        if shift_value is not None:
            self[self.SH_C2] = shift_value

    def set_constant(self, constant: Constant):
        if constant.is_const3():
            return self.set_const3(constant)

        match self.constant_index:
            case 0:
                self.set_const1(constant)
            case 1:
                self.set_const2(constant)
            case _:
                raise ValueError(f"Too many constants: {self.constant_index + 1}")
        self.constant_index += 1

    def set_a_input(self, space: int, reg_number: int, shift_value: int = None, significant_count: int = None):
        match space:
            case 1:
                mux_param = self.A1
                trunc_param = self.TR_R1
                shift_param = self.SH_R1
            case 2:
                mux_param = self.A2
                trunc_param = self.TR_R2
                shift_param = self.SH_R2
            case 3:
                mux_param = self.A3
                trunc_param = self.TR_R3
                shift_param = self.SH_R3
            case 4:
                mux_param = self.A4
                trunc_param = self.TR_R4
                shift_param = self.SH_R4
            case _:
                raise ValueError(f"Invalid space: {space}")

        self[mux_param] = reg_number
        if significant_count is not None:
            self[trunc_param] = significant_count
        if shift_value is not None:
            self[shift_param] = shift_value

    def set_input(self, reg_name: InputName, shift_value: int = None, significant_count: int = 32):
        # Определяем, куда вместится вход
        fit_space = []
        match reg_name:
            case InputName.V1:
                fit_space = [2, 1, 4]
            case InputName.V1H:
                fit_space = [3]
            case InputName.V2:
                fit_space = [1, 2, 3, 4]
            case InputName.V3:
                fit_space = [1, 2, 3, 4]
            case InputName.V4:
                fit_space = [1, 2, 3]
            case InputName.R0:
                fit_space = [4]

        found_space = set(self.free_spaces).intersection(fit_space)
        if len(found_space) == 0:
            raise ValueError(f"No free space for input {reg_name}")
        chosen_space = list(found_space)[0]
        self.free_spaces.remove(chosen_space)
        self.set_a_input(chosen_space, 0, shift_value, significant_count)

    def set_rev_reg(self):
        self[self.REV_REG] = True

    def set_rev_txt(self):
        self[self.REV_TXT] = True
