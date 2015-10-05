# casm.py - Cycsi Assembler

import sys
from Parser import Parser

DEBUG = False
fname = ''

def usage():
    print("casm [-d] cal_file_name[.cal]")
    sys.exit()

def parse_args():
    global DEBUG, fname
    nargs = len(sys.argv)

    # too few or too many args
    if nargs < 2 or nargs > 3:
        usage()

    # see if only deebug flag is set
    if nargs == 2 and sys.argv[1].startswith('-'):
        usage()
    else:
        fname = sys.argv[1]
        DEBUG = False

    if nargs == 3:
        if not sys.argv[1].startswith('-'):
            usage()
        if sys.argv[1] == '-d':
            DEBUG = True
        fname = sys.argv[2]
    try:
        b,e = fname.split('.')
        fname = b
    except ValueError:
        pass

def main():
    parse_args()
    print("debug:", DEBUG)
    print("file to process:", fname)
    parser = Parser()
    parser.load(fname)
    parser.run()


if __name__ == '__main__':
    main()


