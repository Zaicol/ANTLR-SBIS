from models.exceptions.AssemblerError import AssemblerError


class AssemblerSyntaxError(AssemblerError):
    """Raised when assembly syntax is invalid."""
    pass
