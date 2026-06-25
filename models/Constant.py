from models.enums.ConfigEnums import BPDAddress
from models.enums.InstructionEnums import ServiceRegister


class Constant:
    address: int | None
    shift: int | None
    reg: ServiceRegister | None
    bpd: BPDAddress | None

    def __init__(self):
        self.address = None
        self.shift = None
        self.reg = None
        self.bpd = None

    def __repr__(self) -> str:
        return f"Constant(address={self.address}, shift={self.shift}, reg={self.reg}, bpd={self.bpd})"

    def set_address(self, address: int):
        self.address = address

    def set_shift(self, shift: int):
        self.shift = shift

    def set_reg(self, reg: ServiceRegister):
        self.reg = reg

    def set_bpd(self, bpd: BPDAddress):
        self.bpd = bpd

    def get_address(self) -> int | None:
        return self.address

    def get_shift(self) -> int | None:
        return self.shift

    def get_reg(self) -> ServiceRegister | None:
        return self.reg

    def get_bpd(self) -> BPDAddress | None:
        return self.bpd

    def is_const3(self) -> bool:
        return self.reg is None and self.address is None
