#############################################
# File Name: ASMInst.py
# Author: W-Mai
# Mail: 1341398182@qq.com
# Created Time:  2022-05-05
#############################################

class ASMInstBase(object):
    def __init__(self, **kwargs):
        self.inst_type = None
        self.inst_name = None
        self.inst_args = None

        self.block = None

        self._kwargs = kwargs

    def _build(self):
        for arg in self.inst_args:
            val = self._kwargs.get(arg, None)
            if val is None:
                raise Exception("Argument %s is not provided." % arg)
            if not self._validator(arg)(val):
                raise Exception("Argument %s is invalid." % arg)
            setattr(self, arg, val)

    def bitcode(self, bit_sep=''):
        if self.inst_type == 'R':
            return bit_sep.join([
                f"{self.func7:07b}",
                f"{self.rs2:05b}",
                f"{self.rs1:05b}",
                f"{self.func3:03b}",
                f"{self.rd:05b}",
                f"{self.opcode:07b}"])
        elif self.inst_type == 'I':
            return bit_sep.join([
                f"{self.imm:012b}",
                f"{self.rs1:05b}",
                f"{self.func3:03b}",
                f"{self.rd:05b}",
                f"{self.opcode:07b}"])
        elif self.inst_type == 'U':
            return bit_sep.join([
                f"{self.imm:020b}",
                f"{self.rd:05b}",
                f"{self.opcode:07b}"])
        elif self.inst_type == 'J':
            return bit_sep.join([
                f"{self.imm:020b}",
                f"{self.rd:05b}",
                f"{self.opcode:07b}"])

        return ""

    def comment(self):
        if self.inst_type == 'R':
            return f"{self.inst_name:8}" + '\t'.join([f"{inst}: {getattr(self, inst)}" for inst in self.inst_args])
        if self.inst_type == 'I':
            return f"{self.inst_name:8}" + '\t'.join([f"{inst}: {getattr(self, inst)}" for inst in self.inst_args])
        if self.inst_type == 'U':
            return f"{self.inst_name:8}" + '\t'.join([f"{inst}: {getattr(self, inst)}" for inst in self.inst_args])
        if self.inst_type == 'J':
            return f"{self.inst_name:8}" + '\t'.join([f"{inst}: {getattr(self, inst)}" for inst in self.inst_args])

    def description(self):
        return ""

    def _validator(self, arg_name) -> "(x: Any) -> bool":
        return lambda x: True


class RTypeInst(ASMInstBase):
    def __init__(self, opcode, func3, func7, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = 'R'
        self.inst_name = 'RTypeInst'
        self.inst_args = ['rd', 'rs1', 'rs2']

        self.opcode = opcode
        self.func3 = func3
        self.func7 = func7

        self._build()

    def _validator(self, arg_name) -> "(x: Any) -> bool":
        return {
            'rd': lambda x: 0 <= x <= 31,
            'rs1': lambda x: 0 <= x <= 31,
            'rs2': lambda x: 0 <= x <= 31,
        }[arg_name]


class ITypeInst(ASMInstBase):
    def __init__(self, opcode, func3, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = 'I'
        self.inst_name = 'ITypeInst'
        self.inst_args = ['rd', 'rs1', 'imm']

        self.opcode = opcode
        self.func3 = func3

        self._build()

        self.imm = self.imm & 0xfff

    def _validator(self, arg_name) -> "(x: Any) -> bool":
        return {
            'rd': lambda x: 0 <= x <= 31,
            'rs1': lambda x: 0 <= x <= 31,
            'imm': lambda x: -2048 <= x <= 2047 or 0 <= x <= 4095,
        }[arg_name]


class UTypeInst(ASMInstBase):
    def __init__(self, opcode, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = 'U'
        self.inst_name = 'UTypeInst'
        self.inst_args = ['rd', 'imm']

        self.opcode = opcode

        self._build()

        self.imm_ = self.imm << 12
        self.imm = self.imm & 0xfffff

    def _validator(self, arg_name) -> "(x: Any) -> bool":
        return {
            'rd': lambda x: 0 <= x <= 31,
            'imm': lambda x: -2 ** 19 <= x <= 2 ** 19 - 1 or 0 <= x <= 2 ** 20 - 1,
        }[arg_name]


class JTypeInst(ASMInstBase):
    def __init__(self, opcode, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = 'J'
        self.inst_name = 'JTypeInst'
        self.inst_args = ['rd', 'imm']

        self.opcode = opcode

        self._build()

        self.imm_ = self.imm
        self.imm = (self.imm & 0b111111111111111111111) >> 1
        part4 = (self.imm & 0b10000000000000000000) >> 19 << 19
        part3 = (self.imm & 0b01111111100000000000) >> 11
        part2 = (self.imm & 0b00000000010000000000) >> 10 << 8
        part1 = (self.imm & 0b00000000001111111111) << 9

        self.imm = part4 | part1 | part2 | part3

    def _validator(self, arg_name) -> "(x: Any) -> bool":
        return {
            'rd': lambda x: 0 <= x <= 31,
            'imm': lambda x: -2 ** 19 <= x <= 2 ** 19 - 1 or 0 <= x <= 2 ** 20 - 1,
        }[arg_name]


# ######################### RTypeInst ##########################################

class ADD(RTypeInst):
    def __init__(self, **kwargs):
        super().__init__(func7=0b0000000, func3=0b000, opcode=0b0110011, **kwargs)
        self.inst_name = 'add'

    def description(self):
        return f"R{self.rd} = R{self.rs1} + R{self.rs2}"


class SUB(RTypeInst):
    def __init__(self, **kwargs):
        super().__init__(func7=0b0100000, func3=0b000, opcode=0b0110011, **kwargs)
        self.inst_name = 'sub'

    def description(self):
        return f"R{self.rd} = R{self.rs1} - R{self.rs2}"


class XOR(RTypeInst):
    def __init__(self, **kwargs):
        super().__init__(func7=0b0000000, func3=0b100, opcode=0b0110011, **kwargs)
        self.inst_name = 'xor'

    def description(self):
        return f"R{self.rd} = R{self.rs1} ^ R{self.rs2}"


class OR(RTypeInst):
    def __init__(self, **kwargs):
        super().__init__(func7=0b0000000, func3=0b110, opcode=0b0110011, **kwargs)
        self.inst_name = 'or'

    def description(self):
        return f"R{self.rd} = R{self.rs1} | R{self.rs2}"


class AND(RTypeInst):
    def __init__(self, **kwargs):
        super().__init__(func7=0b0000000, func3=0b111, opcode=0b0110011, **kwargs)
        self.inst_name = 'and'

    def description(self):
        return f"R{self.rd} = R{self.rs1} & R{self.rs2}"


class SLL(RTypeInst):
    def __init__(self, **kwargs):
        super().__init__(func7=0b0000000, func3=0b001, opcode=0b0110011, **kwargs)
        self.inst_name = 'sll'

    def description(self):
        return f"R{self.rd} = R{self.rs1} << R{self.rs2}"


class SRL(RTypeInst):
    def __init__(self, **kwargs):
        super().__init__(func7=0b0000000, func3=0b101, opcode=0b0110011, **kwargs)
        self.inst_name = 'srl'

    def description(self):
        return f"R{self.rd} = R{self.rs1} >> R{self.rs2}"


class SRA(RTypeInst):
    def __init__(self, **kwargs):
        super().__init__(func7=0b0100000, func3=0b101, opcode=0b0110011, **kwargs)
        self.inst_name = 'sra'

    def description(self):
        return f"R{self.rd} = R{self.rs1} >> R{self.rs2}"


class SLT(RTypeInst):
    def __init__(self, **kwargs):
        super().__init__(func7=0b0000000, func3=0b010, opcode=0b0110011, **kwargs)
        self.inst_name = 'slt'

    def description(self):
        return f"R{self.rd} = (R{self.rs1} < R{self.rs2}) ? 1 : 0"


class SLTU(RTypeInst):
    def __init__(self, **kwargs):
        super().__init__(func7=0b0000000, func3=0b011, opcode=0b0110011, **kwargs)
        self.inst_name = 'sltu'

    def description(self):
        return f"R{self.rd} = (R{self.rs1} < R{self.rs2}) ? 1 : 0"


# ######################### ITypeInst ##########################################

class ADDI(ITypeInst):
    def __init__(self, **kwargs):
        super().__init__(func3=0b000, opcode=0b0010011, **kwargs)
        self.inst_name = 'addi'

    def description(self):
        return f"R{self.rd} = R{self.rs1} + {self.imm}"


class XORI(ITypeInst):
    def __init__(self, **kwargs):
        super().__init__(func3=0b100, opcode=0b0010011, **kwargs)
        self.inst_name = 'xori'

    def description(self):
        return f"R{self.rd} = R{self.rs1} ^ {self.imm}"


class ORI(ITypeInst):
    def __init__(self, **kwargs):
        super().__init__(func3=0b110, opcode=0b0010011, **kwargs)
        self.inst_name = 'ori'

    def description(self):
        return f"R{self.rd} = R{self.rs1} | {self.imm}"


class ANDI(ITypeInst):
    def __init__(self, **kwargs):
        super().__init__(func3=0b111, opcode=0b0010011, **kwargs)
        self.inst_name = 'andi'

    def description(self):
        return f"R{self.rd} = R{self.rs1} & {self.imm}"


class SLLI(ITypeInst):
    def __init__(self, **kwargs):
        super().__init__(func3=0b001, opcode=0b0010011, **kwargs)
        self.inst_name = 'slli'

    def description(self):
        return f"R{self.rd} = R{self.rs1} << {self.imm}"

    def _build(self):
        super()._build()
        self.imm = 0b000_0000_11111 & self.imm

    def _validator(self, arg_name) -> "(x: Any) -> bool":
        return {
            'imm': lambda x: 0b000_0000_11111 & x == x
        }.get(arg_name, super()._validator(arg_name))


class SRLI(ITypeInst):
    def __init__(self, **kwargs):
        super().__init__(func3=0b101, opcode=0b0010011, **kwargs)
        self.inst_name = 'srli'

    def description(self):
        return f"R{self.rd} = R{self.rs1} >> {self.imm}"

    def _build(self):
        super()._build()
        self.imm = 0b000_0000_11111 & self.imm

    def _validator(self, arg_name) -> "(x: Any) -> bool":
        return {
            'imm': lambda x: 0b000_0000_11111 & x == x
        }.get(arg_name, super()._validator(arg_name))


class SRAI(ITypeInst):
    def __init__(self, **kwargs):
        super().__init__(func3=0b101, opcode=0b0010011, **kwargs)
        self.inst_name = 'srai'

    def description(self):
        return f"R{self.rd} = R{self.rs1} >> {self.imm}"

    def bitcode(self, bit_sep=''):
        self.imm = 0b000_0000_11111 & self.imm | 0b010_0000_00000
        bits = super().bitcode(bit_sep)
        self.imm = self.imm & 0b000_0000_11111
        return bits

    def _validator(self, arg_name) -> "(x: Any) -> bool":
        return {
            'imm': lambda x: 0b000_0000_11111 & x == x
        }.get(arg_name, super()._validator(arg_name))


class SLTI(ITypeInst):
    def __init__(self, **kwargs):
        super().__init__(func3=0b010, opcode=0b0010011, **kwargs)
        self.inst_name = 'slti'

    def description(self):
        return f"R{self.rd} = (R{self.rs1} < {self.imm}) ? 1 : 0"


class SLTIU(ITypeInst):
    def __init__(self, **kwargs):
        super().__init__(func3=0b011, opcode=0b0010011, **kwargs)
        self.inst_name = 'sltiu'

    def description(self):
        return f"R{self.rd} = (R{self.rs1} < {self.imm}) ? 1 : 0"


class JALR(ITypeInst):
    def __init__(self, **kwargs):
        super().__init__(func3=0b000, opcode=0b1100111, **kwargs)
        self.inst_name = 'jalr'

    def description(self):
        return f"R{self.rd} = PC + 4; PC = R{self.rs1} + {self.imm}"


# ######################### JTypeInst ##########################################

class JAL(JTypeInst):
    def __init__(self, **kwargs):
        super().__init__(opcode=0b1101111, **kwargs)
        self.inst_name = 'jal'

    def description(self):
        return f"R{self.rd} = PC +4 ; PC += {self.imm_}"


# ######################### UTypeInst ##########################################

class LUI(UTypeInst):
    def __init__(self, **kwargs):
        super().__init__(opcode=0b0110111, **kwargs)
        self.inst_name = 'lui'

    def description(self):
        return f"R{self.rd} = {self.imm_}"


class AUIPC(UTypeInst):
    def __init__(self, **kwargs):
        super().__init__(opcode=0b0010111, **kwargs)
        self.inst_name = 'auipc'

    def description(self):
        return f"R{self.rd} = PC + {self.imm_}"
