#############################################
# File Name: ASMBlock.py
# Author: W-Mai
# Mail: 1341398182@qq.com
# Created Time:  2022-05-05
#############################################
from typing import List

from RiscVAssembler.ASMInst import ASMInstBase


class ASMBlockMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        if attrs.get('INSTS', None) is None:
            raise Exception('ASMBlock must have INSTS')

        obj = super().__new__(mcs, name, bases, attrs)

        return obj


class ASMBlock(object, metaclass=ASMBlockMetaclass):
    INSTS: List[ASMInstBase] = []

    @classmethod
    def bitcode(cls,
                bit_sep='',
                need_comment=False,
                comment_sep='//',
                need_description=False,
                description_sep='|') -> str:
        return "\n".join([f"{inst.bitcode(bit_sep=bit_sep):<38}"
                          + (f" {comment_sep} {inst.comment()}" if need_comment else "")
                          + (f" {description_sep} {inst.description()}" if need_description else "")
                          for inst in cls.INSTS])
