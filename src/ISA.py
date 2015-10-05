# Cycsi Instruction Set Architecture

class ISA(object):

    """
    This is a Python dictionary records, one for each mnemonic. 
    The list in each entry indicates needed operands
    """
    CODES = {
        'UND':  [-1,0,0],       # undefined operator
        'MOV':  [1,1,1],        # data mmovement (op1 <- op2)
        'ADD':  [2,1,1],        # signed addition (op1 + op2)
        'SUB':  [3,1,1],        # signed subtraction (op1 - op2)
        'MUL':  [4,1,1],        # signed multiplication (op1 * op2)
        'DIV':  [5,1,1],        # signed division (op1 / op2)
        'AND':  [6,1,0],        # bitwise an logical and (op1 & op2)
        'OR':   [7,1,0],        # bitwise logical or (op1 | op2)
        'XOR':  [8,1,0],        # bitwise exclusive or (op1 ^ op2)
        'NOT':  [9,1,0],        # notwise not operator (!op1)
        'CMP':  [10,1,1],       # compre, set flags
        'JMP':  [11,1,0],       # jump to op1
        'JNZ':  [12,1,0],       # jump is ZF set
        'JL':   [13,1,0],       # jump is less
        'JLE':  [14,1,0],       # jump if less or equal
        'JG':   [15,1,0],       # jump if greater
        'JGE':  [16,1,0],       # jump if greater or equal
        'JNZ':  [17,1,0],       # jump if not equal
        'CALL': [18,1,0],       # procedure call
        'RET':  [19,0,0],       # procedure return
        'PRT':  [20,1,0],       # output statement
        'IN':   [21,1,0],       # input (user -> op1)
        'HLT':  [22,0,0],       # halt processor
        'DN':   [23,1,0],       # data definition
        '.data':[24,0,0],       # data directive
        '.text':[25,0,0],       # code directive
    }

    REGS = ['R0','R1','R2','R3','R4','R5','R6','R7']

    def get_inst_code(self, mnemonic):
        """ return instruction data for this mnemonic """
        if mnemonic in ISA.CODES:
            return ISA.CODES[mnemonic]
        else:
            return [-1, 0,0]

    def get_reg_code(self, reg):
        """ return register code or -1 """
        if reg in ISA.REGS:
            for c in range(len(ISA.REGS)):
                if ISA.REGS[c] == reg: return c
            return -1

    def classify_operand(self, op):
        """ Return operand type and value or name for lookup later """

        # see of there is no operand
        if op is None: return [0,0]
   
        # see if we have a memory ref
        if op[0] == '[':
            mem_ref = 1
            op = op[1:-1]   # strip off the brackets
        else:
            mem_ref = 0

        # do we have a literal or label
        sign = 1
        if op[0] == '-':
            sign = -1
            op = op[1:]     # strip the sign
        if op.isdigit():
            return [1 + mem_ref, int(op)*sign]
        if op.isalpha():
            return [1 + mem_ref, op]

        # check is this is a register
        if op in ISA.REGS:
            return [3 + mem_ref, op]
    
        # register plus base memory ref
        p = op.split('+')
        if len(p) == 2:
            r = p[0].strip()
            if r in ISA.REGS:
                return [5,int(p[1])]

        return [-1,-1]


if __name__ == '__main__':
    i = ISA()
    print i.CODES
    print 'CALL' in i.CODES
    print i.CODES['CALL']

