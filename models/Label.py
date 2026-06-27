class Label:
    def __init__(self, name: str, source_line: int, address: int = 0):
        self.name = name
        self.source_line = source_line
        self.address = address
