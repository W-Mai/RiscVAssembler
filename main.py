#############################################
# File Name: main.py
# Author: W-Mai
# Mail: 1341398182@qq.com
# Created Time:  2022-05-05
#############################################

from RiscVAssembler.ASMInst import (
    ADD, SUB, XOR, OR, AND, SLL, SRL, SRA, SLT, SLTU,
    ADDI, XORI, ORI, ANDI, SLLI, SRLI, SRAI, SLTI, SLTIU,
)
from RiscVAssembler.ASMBlock import ASMBlock


class ASMFile(ASMBlock):
    INSTS = [
        ADD(rd=29, rs1=27, rs2=28),
        SUB(rd=29, rs1=27, rs2=29),
        XOR(rd=29, rs1=27, rs2=29),
        OR(rd=29, rs1=27, rs2=29),
        AND(rd=29, rs1=27, rs2=29),
        SLL(rd=29, rs1=27, rs2=29),
        SRL(rd=29, rs1=27, rs2=29),
        SRA(rd=29, rs1=27, rs2=29),
        SLT(rd=29, rs1=27, rs2=29),
        SLTU(rd=29, rs1=27, rs2=29),

        ADDI(rd=27, rs1=0, imm=0b11011),
        XORI(rd=29, rs1=27, imm=0b00101),
        ORI(rd=29, rs1=27, imm=0b00101),
        ANDI(rd=29, rs1=27, imm=0b00101),
        SLLI(rd=29, rs1=27, imm=2),
        SRLI(rd=29, rs1=27, imm=2),

        ADDI(rd=27, rs1=0, imm=0xfff),
        SRLI(rd=29, rs1=27, imm=2),
        SRAI(rd=29, rs1=27, imm=2),
        SLTI(rd=29, rs1=27, imm=0b11010),
        SLTIU(rd=29, rs1=27, imm=0b11010),

    ]


print(ASMFile.bitcode(bit_sep="_", need_comment=True, need_description=True))
