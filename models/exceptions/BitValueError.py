from models.exceptions.AssemblerError import AssemblerError


class BitValueError(AssemblerError):
    """Raised when an invalid value is assigned to a bit or bit-field."""
    pass
