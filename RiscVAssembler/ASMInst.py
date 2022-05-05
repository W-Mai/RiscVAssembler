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

    def comment(self):
        if self.inst_type == 'R':
            return self.inst_name + '\t' + '\t'.join([f"{inst}: {getattr(self, inst)}" for inst in self.inst_args])

    def description(self):
        return ""

