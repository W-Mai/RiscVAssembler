#############################################
# File Name: main.py
# Author: W-Mai
# Mail: 1341398182@qq.com
# Created Time:  2022-05-05
#############################################

from RiscVAssembler.ASMInst import ASMInstBase, ADD
from RiscVAssembler.ASMBlock import ASMBlock


class ASMFile(ASMBlock):
    INSTS = [
        ADD(rd=29, rs1=27, rs2=28),
        ADD(rd=29, rs1=27, rs2=29),
        ADD(rd=29, rs1=27, rs2=29),
        ADD(rd=29, rs1=27, rs2=29),
        ADD(rd=29, rs1=27, rs2=29),
        ADD(rd=29, rs1=27, rs2=29),
        ADD(rd=29, rs1=27, rs2=29),
    ]


print(ASMFile.bitcode(bit_sep="_", need_comment=True, need_description=True))
