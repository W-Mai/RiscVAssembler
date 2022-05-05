## RiscVAssembler

这是一个基于python的RiscV汇编器。

使用方法也是非常的简单

如下代码所示：

```python
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
```

通过上面的代码，可以得到如下的结果：
```text
0000000_11100_11011_000_11101_0110011  // add     rd: 29	rs1: 27	rs2: 28 | R29 = R27 + R28
0100000_11101_11011_000_11101_0110011  // sub     rd: 29	rs1: 27	rs2: 29 | R29 = R27 - R29
0000000_11101_11011_100_11101_0110011  // xor     rd: 29	rs1: 27	rs2: 29 | R29 = R27 ^ R29
0000000_11101_11011_110_11101_0110011  // or      rd: 29	rs1: 27	rs2: 29 | R29 = R27 | R29
0000000_11101_11011_111_11101_0110011  // and     rd: 29	rs1: 27	rs2: 29 | R29 = R27 & R29
0000000_11101_11011_001_11101_0110011  // sll     rd: 29	rs1: 27	rs2: 29 | R29 = R27 << R29
0000000_11101_11011_101_11101_0110011  // srl     rd: 29	rs1: 27	rs2: 29 | R29 = R27 >> R29
0100000_11101_11011_101_11101_0110011  // sra     rd: 29	rs1: 27	rs2: 29 | R29 = R27 >> R29
0000000_11101_11011_010_11101_0110011  // slt     rd: 29	rs1: 27	rs2: 29 | R29 = (R27 < R29) ? 1 : 0
0000000_11101_11011_011_11101_0110011  // sltu    rd: 29	rs1: 27	rs2: 29 | R29 = (R27 < R29) ? 1 : 0
000000011011_00000_000_11011_0010011   // addi    rd: 27	rs1: 0	imm: 27 | R27 = R0 + 27
000000000101_11011_100_11101_0010011   // xori    rd: 29	rs1: 27	imm: 5 | R29 = R27 ^ 5
000000000101_11011_110_11101_0010011   // ori     rd: 29	rs1: 27	imm: 5 | R29 = R27 | 5
000000000101_11011_111_11101_0010011   // andi    rd: 29	rs1: 27	imm: 5 | R29 = R27 & 5
000000000010_11011_001_11101_0010011   // slli    rd: 29	rs1: 27	imm: 2 | R29 = R27 << 2
000000000010_11011_101_11101_0010011   // srli    rd: 29	rs1: 27	imm: 2 | R29 = R27 >> 2
111111111111_00000_000_11011_0010011   // addi    rd: 27	rs1: 0	imm: 4095 | R27 = R0 + 4095
000000000010_11011_101_11101_0010011   // srli    rd: 29	rs1: 27	imm: 2 | R29 = R27 >> 2
010000000010_11011_101_11101_0010011   // srai    rd: 29	rs1: 27	imm: 2 | R29 = R27 >> 2
000000011010_11011_010_11101_0010011   // slti    rd: 29	rs1: 27	imm: 26 | R29 = (R27 < 26) ? 1 : 0
000000011010_11011_011_11101_0010011   // sltiu   rd: 29	rs1: 27	imm: 26 | R29 = (R27 < 26) ? 1 : 0
```