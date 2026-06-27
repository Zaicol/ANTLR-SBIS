from models.ProgInstruction import ProgInstruction


class LastInstruction:
    def __init__(self, idx: int, instruction: ProgInstruction):
        self.idx = idx
        self.instruction = instruction
        self.cycles_since = 0

    def add_cycles(self, cycles: int):
        self.cycles_since += cycles

    def get_index(self) -> int:
        return self.idx

    def get_instruction(self) -> ProgInstruction:
        return self.instruction

    def get_cycles_since(self) -> int:
        return self.cycles_since
