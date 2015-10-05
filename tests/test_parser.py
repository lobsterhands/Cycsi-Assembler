import unittest
import sys
sys.path.insert(0, 'src')
from Parser import Parser, ParserError

class Test_Parser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_empty_file(self):
        """ test that we start with no lines """
        self.assertEquals(len(self.parser.lines), 0)

    def test_file_loading(self):
        """ test file has 24 lines """
        self.parser.load('tests/test.cal')
        self.assertEquals(len(self.parser.lines), 24)

    def test_parse_empty_line(self):
        """ test that parsing a blans line returns 4 None values """
        self.assertEquals(self.parser.parse_line(''), [None, None, None, None])

    def test_ignore_comment_line(self):
        """ test that we ignore comments """
        tline = "  ;  This is a comment line"
        self.assertEquals(self.parser.parse_line(tline), [None, None, None, None])

    def test_labels(self):
        """ test that we spot labels properly """
        tline1 = "  label:  MOV This is a labeled line"
        tline2 = "  This line has no label"
        self.assertEquals(self.parser.parse_line(tline1)[0]['addr'], 0)
        self.assertEquals(self.parser.parse_line(tline2)[0], None)

    def test_duplicate_label_error(self):
        """ test that duplicate labes raise an exception """
        tline1 = "  label:  This is a labeled line"
        tline2 = ' label:'
        self.parser.parse_line(tline1)
        self.assertRaises(ParserError, self.parser.parse_line, tline2)

    def test_operand_classifier(self):
        self.parser.p = '1234'
        self.assertEqual(self.parser.check_operand()[0],1) 
        self.parser.p = 'label'
        self.assertEqual(self.parser.check_operand()[0],1) 
        self.parser.p = '[1234]'
        self.assertEqual(self.parser.check_operand()[0],2) 
        self.parser.p = '[label]'
        self.assertEqual(self.parser.check_operand()[0],2) 
        self.parser.p = 'R2'
        self.assertEqual(self.parser.check_operand()[0],3) 
        self.parser.p = '[R2]'
        self.assertEqual(self.parser.check_operand()[0],4) 
        self.parser.p = '[R2+5]'
        self.assertEqual(self.parser.check_operand()[0],5) 
        self.parser.p = '[R2 + 5]'
        self.assertEqual(self.parser.check_operand()[0],5) 

if __name__ == '__main__':
    unittest.main()
