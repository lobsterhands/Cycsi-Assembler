# Test Symbol Table

import unittest
import sys
sys.path.insert(0, 'src')
from SymTable import SymTable, SymbolError

class Test_Sym_Table(unittest.TestCase):

    def setUp(self):
        self.symtab = SymTable()

    def test_new_symbol(self):
        """ test that a new symbol is accepted """
        self.symtab.add('label1',0,1)
        self.assertEquals(self.symtab.get('label1')['name'],'label1')

    def test_duplicate_symbol(self):
        """ test that a duplicate symbol is rejected"""
        self.symtab.add('label2',0,1)
        self.assertRaises(SymbolError, self.symtab.add,'label2',0,1)

    def test_return_unknown_symbol(self):
        """ test that an unknown symbol returns None"""
        self.assertEquals(self.symtab.get('XXX'), None)

if __name__ == '__main__':
    unittest.main()
