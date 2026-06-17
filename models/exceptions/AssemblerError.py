class AssemblerError(Exception):
    """Базовое исключение для ассемблера"""

    def __init__(self, message: str, line: int = None, column: int = None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        parts = [self.message]
        if self.line is not None:
            location = f"line {self.line}"
            if self.column is not None:
                location += f", column {self.column}"
            parts.append(f"at {location}")
        return " ".join(parts)
