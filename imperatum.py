from impmath import *
MEM_variables = dict()
MEM_next = 0
def var_preprocessor(variable):
    if (variable in MEM_variables):
        return MEM_variables[variable]
    else:
        MEM_variables[variable] = MEM_next
        MEM_next += 1
        return MEM_variables[variable]


code = "code insert goes here"


instructions = {"end": 0x00, "number": 0x01, "word": 0x02, "truth": 0x03, "true": 0x04,"false": 0x05,"is": 0x06,"if": 0x07,"then": 0x08,"else": 0x09,"for": 0x0A,"while": 0x0B,"each": 0x0C,"and": 0x0D,"or": 0x0E,"xor": 0x0F}

MEM_numbers = []
MEM_words = []


def read(table, n, value):
    if (len(table) < n):
        table[n]=value
    else:
        table += [value]
    n += 1
    return

print LNumAdd(intToLNum(5),intToLNum(2))
print LNumSub(intToLNum(5),intToLNum(1))
print LNumMul(intToLNum(54),intToLNum(23))

print " ".join('hello')
def getNum(var):
    return nums[var_preprocessor(var)]

def setNum(var, val):
    nums[var_preprocessor(var)] = val
    return

def getWord(var):
    return words[var_preprocessor(var)]

def setWord(var, val):
    words[var_preprocessor(var)] = val
    return

values = []
pc = 0
read(values,pc,"potato")
read(values,pc," is")
read(values,pc,"KAWAII!!!")
print values

def hello(this):
    print "hello, world!"
    return this
def main():
    print hello("Again!")
    return 0
if __name__ == '__main__':
    main()
