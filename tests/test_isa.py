import unittest
import sys
sys.path.insert(0, 'src')
from ISA import ISA

class Test_ISA(unittest.TestCase):

    def setUp(self):
        """ create an ISA object for testing """
        self.isa = ISA()

    def test_inst_code(self):
        """ test that an undefined mnemonic returns the error code """
        self.assertEqual(self.isa.get_inst_code('UNDEF')[0], -1)

    def test_basic_inst_lookup(self):
        """ test that we get the right data for an example instruction """
        self.assertEqual(self.isa.get_inst_code('MOV')[0], 1)
        self.assertEqual(self.isa.get_inst_code('MOV')[1], 1)
        self.assertEqual(self.isa.get_inst_code('MOV')[2], 1)

if __name__ == '__main__':
    unittest.main()
