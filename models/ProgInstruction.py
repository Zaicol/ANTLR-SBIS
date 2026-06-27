from models.Label import Label
from models.enums.InstructionEnums import *
from models.MachineInstruction import MachineInstruction


class ProgInstruction(MachineInstruction):

    START_GEN = 0
    WROUT = 1
    RD = 2
    CMP = 3
    CONF_ADDR = slice(9, 4, -1)

    TRANSFORMATION_TYPE_MODE = slice(14, 12, -1)
    TRANSFORMATION_TYPE = 15

    MASK_WBUF = slice(19, 16, -1)
    MASK_WBUF_BPD1 = 16  # V1
    MASK_WBUF_BPD2 = 17  # V2
    MASK_WBUF_BPD3 = 18  # V3
    MASK_WBUF_BPD4 = 19  # V4
    EN_XOR = 20  # V2^
    EN_AND = 21  # V4&
    OUTPUT = slice(21, 16, -1)

    INSTRUCION_TYPE = 24

    SERVICE_TYPE = slice(26, 25, -1)
    REG_INIT_VALUE = slice(23, 0, -1)
    REG_ARG_NUM = slice(1, 0, -1)
    JMP_ADDR = slice(7, 0, -1)

    WAIT_FLAG = 27
    EXPRESSION_VALUE = slice(7, 0, -1)

    REG_NUM = slice(29, 28, -1)
    INC = 30
    EOP = 31

    CONTROL_FIELDS = slice(21, 12, -1)

    def __init__(self, source_line: int = 0):
        super().__init__(source_line=source_line)
        self.label: Label | None = None
        self.jump_label: Label | None = None
        self.latency: int = 0

    def set_start_gen(self):
        self[self.START_GEN] = True

    def set_wrout(self):
        self[self.WROUT] = True

    def set_rd(self):
        self[self.RD] = True

    def set_cmp(self):
        self[self.CMP] = True

    def set_config_addr(self, addr: int):
        self[self.CONF_ADDR] = addr

    def set_transformation(self, transformation_type: TransformationType):
        self[self.TRANSFORMATION_TYPE] = transformation_type.value
        self.set_rd()

    def set_sp_op(self, sp_op: SPType):
        self[self.TRANSFORMATION_TYPE_MODE] = sp_op.value
        self.set_transformation(TransformationType.SP)
        self.set_sp_latency(sp_op)

    def set_alu_op(self, alu_op: ALUType):
        self[self.TRANSFORMATION_TYPE_MODE] = alu_op.value
        self.set_transformation(TransformationType.ALU)
        self.set_alu_latency()

    def set_output(self, output_list: list[OutputPlaces]):
        output = 0
        for place in output_list:
            if place == OutputPlaces.CMP:
                self.set_cmp()     # бит cmp находится в другом месте инструкции
            output |= place.value  # Побитово собираем все места, куда записывать вывод (v1-v4, v2^, v4&)
        self[self.OUTPUT] = output

    def set_operation_type(self, operation_type: InstructionType):
        self[self.INSTRUCION_TYPE] = operation_type.value

    def set_service_operation_type(self, service_type: ServiceType):
        self[self.SERVICE_TYPE] = service_type.value

    def set_arg_num(self, arg_num: int):
        self[self.REG_ARG_NUM] = arg_num

    def set_reg_init_value(self, value: int):
        self[self.REG_INIT_VALUE] = value

    def set_wait(self):
        self[self.WAIT_FLAG] = True

    def set_label_addr(self, addr: int):
        self[self.JMP_ADDR] = addr

    def set_expression_value(self, value: int):
        self[self.EXPRESSION_VALUE] = value

    def set_service_reg(self, service_reg: ServiceRegister):
        self[self.REG_NUM] = service_reg.value

    def set_increment(self):
        self.set_operation_type(InstructionType.SERVICE)
        self.set_service_operation_type(ServiceType.INC_DEC)
        self[self.INC] = True

    def set_decrement(self):
        self.set_operation_type(InstructionType.SERVICE)
        self.set_service_operation_type(ServiceType.INC_DEC)
        self[self.INC] = False

    def set_eop(self):
        self[self.EOP] = True

    # ===================== BOOLEAN МЕТОДЫ =====================
    # === БАЗОВЫЕ ПРИЗНАКИ ===

    def is_standard(self) -> bool:
        return self[self.INSTRUCION_TYPE] == InstructionType.STANDARD

    def is_service(self) -> bool:
        return self[self.INSTRUCION_TYPE] == InstructionType.SERVICE

    def is_active(self) -> bool:
        is_std = self.is_standard()
        is_act = self[self.RD] == 1
        return is_std and is_act

    def is_passive(self) -> bool:
        is_std = self.is_standard()
        is_pas = self[self.RD] == 0
        return is_std and is_pas

    def is_wait(self) -> bool:
        is_serv = self.is_service()
        is_wait = self[self.WAIT_FLAG] == 1
        return is_serv and is_wait

    def is_eop(self) -> bool:
        is_serv = self.is_service()
        is_eop = self[self.EOP] == 1
        return is_serv and is_eop

    def is_jump(self) -> bool:
        return self[self.SERVICE_TYPE] == ServiceType.JNZ.value

    # === ОПЕРАЦИИ С ДАННЫМИ ===

    def is_start_gen(self) -> bool:
        return self[self.START_GEN] == 1

    def is_wrout(self) -> bool:
        return self[self.WROUT] == 1

    # === СОСТАВНЫЕ ПРИЗНАКИ ДЛЯ WAIT ===

    def is_active_standard(self) -> bool:
        return self.is_standard() and self.is_active()

    def get_wait(self):
        if not self.is_wait():
            return 0
        return self[self.EXPRESSION_VALUE]

    def set_label(self, label: Label):
        self.label = label

    def get_label(self) -> Label | None:
        return self.label

    def set_jump_label(self, label: Label):
        self.jump_label = label

    def get_jump_label(self) -> Label | None:
        return self.jump_label

    def is_labeled(self) -> bool:
        return self.label is not None

    def set_sp_latency(self, sp_type: SPType):
        match sp_type:
            case SPType.A1:
                self.latency = 27
            case SPType.A4:
                self.latency = 17
            case SPType.A5:
                self.latency = 33
            case SPType.A128D:
                self.latency = 20
            case SPType.D, SPType.DINV, SPType.DK64, SPType.DINVK64:
                self.latency = 4

    def set_alu_latency(self):
        self.latency = 1

    def get_latency(self) -> int:
        return self.latency

    def is_passive_standard(self):
        return not self.is_active() and self.is_standard()

    def check_same_instructions(self, other: 'ProgInstruction'):
        return self[self.CONTROL_FIELDS] == other[self.CONTROL_FIELDS]

    def has_v4_in_outputs(self) -> bool:
        is_act_std = self.is_active_standard()
        has_v4 = (self[self.OUTPUT] & OutputPlaces.V4) != 0
        return is_act_std and has_v4
