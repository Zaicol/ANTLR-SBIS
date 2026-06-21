class Constant:
    address: int
    shift: int | None

    def __init__(self, value: int):
        self.address = value
        self.shift = None

    def set_shift(self, shift: int):
        self.shift = shift

    def get_address(self) -> int:
        return self.address

    def get_shift(self) -> int | None:
        return self.shift
