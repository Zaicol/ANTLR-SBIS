from enum import Enum


class TransformationType(Enum):
    SP = 0
    ALU = 1


class SPType(Enum):
    A1 = 0
    A4 = 1
    A5 = 2
    A128D = 3
    D = 4
    DINV = 5
    D_K64 = 6
    DINV_K64 = 7


class ALUType(Enum):
    ID = 0
    AND = 1
    OR = 2
    XOR = 3
    NOT = 4
    REV = 5


class OutputPlaces(Enum):
    # Биты
    V1 = 1
    V2 = 2
    V3 = 4
    V4 = 8
    V2N = 16
    V4M = 32

class InstructionType(Enum):
    SERVICE = 0
    STANDARD = 1


class ServiceType(Enum):
    REG_INIT = 0
    INC_DEC = 1
    REG_ASSIGN = 2
    JNZ = 3


class ServiceRegister(Enum):
    R0 = 0
    R1 = 1
    R2 = 2
    R3 = 3
