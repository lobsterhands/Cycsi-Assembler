# Parser.py - Process a Cycsi assembly language file
import sys

from ISA import ISA
from SymTable import SymTable

class ParserError(Exception):

    def __init__(self, message):
        self.message = message


class Parser(object):

    def __init__(self):
        """ build an initialized Parser """
        self.lines = []
        self.lineno = 1
        self.sym_table = SymTable()
        self.loc_code = 0
        self.loc_data = 0
        self.code_mem = []
        self.data_mem = []
        self.isa = ISA()
        self.inData = True

    def load(self,fname):
        """ load code file for processing """
        self.fbase = fname
        fname = fname + '.cal'
        try:
            self.lines = open(fname,'r').readlines()
        except IOError:
            raise ParserError("Error opening file: %s" % fname)
            sys.exit()

    def run(self):
        print("processing %s.cal" % self.fbase)
        for line in self.lines:
            self.parse_line(line)
        print("\tcomplete...")
        self.writer()

    def writer(self):
        iname = self.fbase + '.imem'
        dname = self.fbase + '.dmem'
        for i in self.code_mem:
            print i
        for d in self.data_mem:
            print d
        print("memory files written")

    def new_symbol(self):
        """ add symbol, error if alaready defined """
        if not self.sym_table.get(self.p) is None:
            raise ParserError("Duplicate Symbol: %s" % self.p)
        if self.inData:
            self.sym_table.add(self.p, self.loc_data, self.lineno)
        else:
            self.sym_table.add(self.p, self.loc_code, self.lineno)

    def check_label(self):
        """ check current symbol is a label, return true is OK, false if not """
        if self.p.endswith(':'):
            self.p = self.p[:-1]
            self.new_symbol()       # check new symbol
            return True
        return False

    def next_sym(self):
        """ fetch next part from list, return True is we have one """
        try:
            self.p = self.parts.pop(0)
            if self.p.startswith(';'): return False
        except IndexError:
            return False
        return True

    def check_operand(self):
        """ classify operand, return [oper_code, value] """
        op = self.p
        if op is None: return [0,0]

        if op[0] == '[':
            mem_ref = 1     # we have a memory reference
            op = op[1:-1]   # strip off brackets
        else:
            mem_ref = 0     # no memory reference

        # check for literal or label
        sign = 1
        if op[0] == '-':
            sign = -1
            op = op[1:]
        if op.isdigit():
            return [1 + mem_ref, op]

        # check if this is a register
        if op in self.isa.REGS:
            return [3 + mem_ref, op]

        # check for label
        if op.isalnum():
            return [1 + mem_ref, op]

        # check for base plus offset
        p = op.split('+')
        if len(p) == 2:
            base = p[0].strip()
            offset = p[1].strip()
            if base in self.isa.REGS:
                return [5, int(offset)]
        return [-1,-1]


    def parse_line(self, line):
        """ check one line, return list:
            [ label_addr, inst_code, op1[], op2[] ]
        """

        result = [None, None, None, None]

        # if line is empty, return
        if len(line) == 0:
            return result

        # split the line into parts
        self.parts = line.split()

        # load the first part: comment, label of mnemonic
        if not self.next_sym(): return result

        # check for directives
        if self.p == '.text':
            self.inData = False
            return
        if self.p == '.data':
            self.inData = True
            return

        if self.check_label():
            # we have a label to process
            result[0] = self.sym_table.get(self.p)
            if not self.next_sym(): return result

        # if we get here, we need a mnemonic
        inst_codes = self.isa.get_inst_code(self.p)

        result[1] = inst_codes[0]

        # process operands if needed
        if inst_codes[1] == 1:
            if not self.next_sym():
                raise ParserError("Missing Operand 1")
            result[2] = self.check_operand()
        if inst_codes[2] == 1:
            if not self.next_sym():
                raise ParserError("Missing Operand 2")
            result[3] = self.check_operand()

        # store results
        if self.inData:
            self.data_mem.append(result)
            self.loc_data += 1
        else:
            self.code_mem.append(result)
            self.loc_code += 1
        return result

if __name__ == '__main__':
    p = Parser()
    p.parse_line('.data')
    p.parse_line('label: DN 5')

    p.parse_line('.text')
    p.parse_line('label2: MOV OP1 R2')
    p.parse_line('Label3: JMP label2')
    p.parse_line('Label4: JMP [R3]')
    p.parse_line('JMP [R4+5]')

    print p.data_mem
    print p.code_mem
