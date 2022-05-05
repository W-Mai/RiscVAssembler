#############################################
# File Name: main.py
# Author: W-Mai
# Mail: 1341398182@qq.com
# Created Time:  2022-05-05
#############################################

from RiscVAssembler.ASMInst import ASMInstBase, ADD, SUB, XOR, OR, AND, SLL, SRL, SRA, SLT, SLTU
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
    ]


print(ASMFile.bitcode(bit_sep="_", need_comment=True, need_description=True))
