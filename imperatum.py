from impmath import *
from imptruth import *
import sys


################################################
#             Latin Interpreter                #
################################################


MEM_variables = dict()
MEM_next = 0
def var_preprocessor(variable):
    if (variable in MEM_variables):
        return MEM_variables[variable]
    else:
        MEM_variables[variable] = MEM_next
        MEM_next += 1
        return MEM_variables[variable]


# File input
CODE_file = open(sys.argv[0],'r')
CODE_dataraw = CODE_file.read()
# Whitespace stripping and list formatting
def stripandformat(a):
    return

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
#Syntax: if [block] then [block] else [block] end
# for [block] each [block] end
# while [block] each [block] end
#TODO: handle end, then, else, each, and, or, xor, true, false
def step():
    global code
    pc = 0
    while pc < len(code):
        if code[pc] == "number":  #Number
            pass
        elif code[pc] == "word":  #Word
            pass
        elif code[pc] == "truth": #Truth
            pass
        elif code[pc] == "is":    #Is
            pass
        elif code[pc] == "if":    #If
            pass
        elif code[pc] == "for":   #For
            pass
        elif code[pc] == "while": #While
            pass
        elif code[pc] == "read":  #Read
            pass
        elif code[pc] == "write": #Write
            pass
        else:
            pass
    return


def main():
    print "main executed."
    return 0
if __name__ == '__main__':
    main()
