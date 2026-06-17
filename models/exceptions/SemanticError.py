from models.exceptions.AssemblerError import AssemblerError


class SemanticError(AssemblerError):
    """Raised when semantic checks fail (e.g., undefined variables, configs)."""

    def __init__(self, identifier: str, message: str = None, line: int = None, column: int = None):
        self.identifier = identifier
        if message is None:
            message = f"Undefined identifier: '{identifier}'"
        super().__init__(message, line, column)
