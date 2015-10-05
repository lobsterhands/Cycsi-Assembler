# Symbol table manager

class SymbolError(Exception):
    
    def __init__(self, message):
        self.message = message


class SymTable(object):

    def __init__(self):
        self.table = {}

    def add(self, label, address, lineno):
        """ record a new label at this address and line no """
        if not self.get(label) is None: 
            raise SymbolError("Duplicate Symbol: %s" % label)
        item = {}
        item['name'] = label
        item['addr'] = address
        item['lines'] = []
        item['lines'].append(lineno)
        self.table[label] = item

    def get(self, label):
        """ return table entry for label, else None """
        if label in self.table:
            return self.table[label]
        return None

if __name__ == '__main__':
    st = SymTable()
    st.add('label',0,1)
    try:
        st.add('label',0,1)
    except SymbolError:
        print "No new dupe"

        
