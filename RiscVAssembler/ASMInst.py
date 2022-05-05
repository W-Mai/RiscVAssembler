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
        if self.inst_type == 'I':
            return bit_sep.join([
                f"{self.imm:012b}",
                f"{self.rs1:05b}",
                f"{self.func3:03b}",
                f"{self.rd:05b}",
                f"{self.opcode:07b}"])

    def comment(self):
        if self.inst_type == 'R':
            return f"{self.inst_name:8}" + '\t'.join([f"{inst}: {getattr(self, inst)}" for inst in self.inst_args])
        if self.inst_type == 'I':
            return f"{self.inst_name:8}" + '\t'.join([f"{inst}: {getattr(self, inst)}" for inst in self.inst_args])

    def description(self):
        return ""


class ADD(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "R"
        self.inst_name = "add"
        self.inst_args = ["rd", "rs1", "rs2"]

        self.opcode = 0b0110011
        self.func3 = 0b000
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} + R{self.rs2}"


class SUB(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "R"
        self.inst_name = "sub"
        self.inst_args = ["rd", "rs1", "rs2"]

        self.opcode = 0b0110011
        self.func3 = 0b000
        self.func7 = 0b0100000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} - R{self.rs2}"


class XOR(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "R"
        self.inst_name = "xor"
        self.inst_args = ["rd", "rs1", "rs2"]

        self.opcode = 0b0110011
        self.func3 = 0b100
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} ^ R{self.rs2}"


class OR(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "R"
        self.inst_name = "or"
        self.inst_args = ["rd", "rs1", "rs2"]

        self.opcode = 0b0110011
        self.func3 = 0b110
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} | R{self.rs2}"


class AND(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "R"
        self.inst_name = "and"
        self.inst_args = ["rd", "rs1", "rs2"]

        self.opcode = 0b0110011
        self.func3 = 0b111
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} & R{self.rs2}"


class SLL(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "R"
        self.inst_name = "sll"
        self.inst_args = ["rd", "rs1", "rs2"]

        self.opcode = 0b0110011
        self.func3 = 0b001
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} << R{self.rs2}"


class SRL(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "R"
        self.inst_name = "srl"
        self.inst_args = ["rd", "rs1", "rs2"]

        self.opcode = 0b0110011
        self.func3 = 0b101
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} >> R{self.rs2}"


class SRA(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "R"
        self.inst_name = "sra"
        self.inst_args = ["rd", "rs1", "rs2"]

        self.opcode = 0b0110011
        self.func3 = 0b101
        self.func7 = 0b0100000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} >> R{self.rs2}"


class SLT(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "R"
        self.inst_name = "slt"
        self.inst_args = ["rd", "rs1", "rs2"]

        self.opcode = 0b0110011
        self.func3 = 0b010
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = (R{self.rs1} < R{self.rs2}) ? 1 : 0"


class SLTU(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "R"
        self.inst_name = "sltu"
        self.inst_args = ["rd", "rs1", "rs2"]

        self.opcode = 0b0110011
        self.func3 = 0b011
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = (R{self.rs1} < R{self.rs2}) ? 1 : 0"


class ADDI(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "I"
        self.inst_name = "addi"
        self.inst_args = ["rd", "rs1", "imm"]

        self.opcode = 0b0010011
        self.func3 = 0b000
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} + {self.imm}"


class XORI(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "I"
        self.inst_name = "xori"
        self.inst_args = ["rd", "rs1", "imm"]

        self.opcode = 0b0010011
        self.func3 = 0b100
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} ^ {self.imm}"


class ORI(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "I"
        self.inst_name = "ori"
        self.inst_args = ["rd", "rs1", "imm"]

        self.opcode = 0b0010011
        self.func3 = 0b110
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} | {self.imm}"


class ANDI(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "I"
        self.inst_name = "andi"
        self.inst_args = ["rd", "rs1", "imm"]

        self.opcode = 0b0010011
        self.func3 = 0b111
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} & {self.imm}"


class SLLI(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "I"
        self.inst_name = "slli"
        self.inst_args = ["rd", "rs1", "imm"]

        self.opcode = 0b0010011
        self.func3 = 0b001
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} << {self.imm}"

    def _build(self):
        super()._build()
        self.imm = 0b000_0000_11111 & self.imm


class SRLI(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "I"
        self.inst_name = "srli"
        self.inst_args = ["rd", "rs1", "imm"]

        self.opcode = 0b0010011
        self.func3 = 0b101
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} >> {self.imm}"

    def _build(self):
        super()._build()
        self.imm = 0b000_0000_11111 & self.imm


class SRAI(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "I"
        self.inst_name = "srai"
        self.inst_args = ["rd", "rs1", "imm"]

        self.opcode = 0b0010011
        self.func3 = 0b101
        self.func7 = 0b0100000

        self._build()

    def description(self):
        return f"R{self.rd} = R{self.rs1} >> {self.imm}"

    def bitcode(self, bit_sep=''):
        self.imm = 0b000_0000_11111 & self.imm | 0b010_0000_00000
        bits = super().bitcode(bit_sep)
        self.imm = self.imm & 0b000_0000_11111
        return bits


class SLTI(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "I"
        self.inst_name = "slti"
        self.inst_args = ["rd", "rs1", "imm"]

        self.opcode = 0b0010011
        self.func3 = 0b010
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = (R{self.rs1} < {self.imm}) ? 1 : 0"


class SLTIU(ASMInstBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inst_type = "I"
        self.inst_name = "sltiu"
        self.inst_args = ["rd", "rs1", "imm"]

        self.opcode = 0b0010011
        self.func3 = 0b011
        self.func7 = 0b0000000

        self._build()

    def description(self):
        return f"R{self.rd} = (R{self.rs1} < {self.imm}) ? 1 : 0"
