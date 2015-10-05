# test_packer.py - Test Instruction Packer

import unittest
import sys
sys.path.insert(0, 'src')
from Packer import Packer

class Test_Packer(unittest.TestCase):

    def setUp(self):
        self.packer = Packer()
        self.inst = 1
        self.reg1 = 2
        self.mode1 = 3
        self.reg2 = 4
        self.mode2 = 5

    def test_pack_inst(self):
        """ test that a new instruction is encoded """
        code = self.packer.pack(
                self.inst,
                self.reg1,
                self.mode1,
                self.reg2, 
                self.mode2)
        self.assertEquals(code, 5349)

    def test_unpack_inst(self):
        self.assertEquals(self.packer.unpack(5349),
                [
                    self.inst,
                    self.reg1,
                    self.mode1,
                    self.reg2,
                    self.mode2
                ]
        )

if __name__ == '__main__':
    unittest.main()
