from models.BitCommand import BitCommand


class LastInstruction:
    def __init__(self, idx: int, instruction: BitCommand):
        self.idx = idx
        self.instruction = instruction
        self.cycles_since = 0

    def add_cycles(self, cycles: int):
        self.cycles_since += cycles

    def get_index(self) -> int:
        return self.idx

    def get_instruction(self) -> BitCommand:
        return self.instruction

    def get_cycles_since(self) -> int:
        return self.cycles_since
