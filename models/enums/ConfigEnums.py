from enum import Enum, IntEnum


class InputSpace(IntEnum):
    A1 = 0
    A2 = 1
    A3 = 2
    A4 = 3


class InputName(Enum):
    V1 = "v1"
    V1H = "v1h"
    V2 = "v2"
    V3 = "v3"
    V4 = "v4"
    R0 = "r0"


class BPDAddress(IntEnum):
    V1 = 0
    V2 = 1
    V3 = 2
    V4 = 3
