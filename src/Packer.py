# Packer.py - handles packing and unpacking instructions

class Packer(object):

    def __init__(self):
        pass

    def pack(self, inst, reg1, mode1, reg2, mode2):
        result = 0
        result += inst << 12
        result += reg1 << 9
        result += mode1 << 6
        result += reg2 << 3
        result += mode2
        return result

    def unpack(self, op):
        inst = (op >> 12) & 0x1f
        reg1 = (op >> 9) & 0x7
        mode1 = (op >> 6) & 0x7
        reg2 = (op >> 3) & 0x7
        mode2 = op & 0x7
        return [inst, reg1, mode1, reg2, mode2]

