from models.exceptions.AssemblerError import AssemblerError


class AssemblerDuplicateError(AssemblerError):
    def __init__(self, identifier: str, message: str = None, line: int = None, column: int = None):
        self.identifier = identifier
        if message is None:
            message = f"Duplicate identifier: '{identifier}'"
        super().__init__(message, line, column)
