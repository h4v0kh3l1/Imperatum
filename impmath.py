from operator import *
"""
Imperatum math functions

Latin numbers (LNums) are represented as strings, of the format "MDCLXVI", with any number ofletters in a row. Normalized form is of the maximum format "MDCCCCLXXXXVIIII", with any number of M's.

Functions provided:
isLNum (number : string) : bool
intToLNum (number : int) : string


"""


    # Helper function for intToLatin
def iTL_help(n,k):
    if (k==1000):
        if (n/1000)==0:
            return iTL_help(n,500)
        else:
            return "M" + iTL_help(n-1000,1000)
    elif (k==500):
        if (n/500)==0:
            return iTL_help(n,100)
        else:
            return "D" + iTL_help(n-500,500)
    elif (k==100):
        if (n/100)==0:
            return iTL_help(n,50)
        else:
            return "C" + iTL_help(n-100,100)
    elif (k==50):
        if (n/50)==0:
            return iTL_help(n,10)
        else:
            return "L" + iTL_help(n-50,50)
    elif (k==10):
        if (n/10)==0:
            return iTL_help(n,5)
        else:
            return "X" + iTL_help(n-10,10)
    elif (k==5):
        if (n/5)==0:
            return iTL_help(n,1)
        else:
            return "V" + iTL_help(n-5,5)
    else:
        if n==0:
            return ""
        else:
            return "I" + iTL_help(n-1,1)

# Takes integer and converts to string LNum
def intToLNum(n):
    if (n < 0):
        return "-" . iTL_help(-n,1000)
    else:
        return iTL_help(n,1000)

def isLNum(n):
    if ("" == (n.replace("M","").replace("D",'').replace('C','').replace('L','').replace('X','').replace('V','').replace('I',''))):
        return 1
    else:
        return 0
# Takes a L-tuple, prints string of LNum
def LTupToLNum(a):
    out = ""
    for x in range(a[0]):
        out = out+"M"
    for x in range(a[1]):
        out = out+"D"
    for x in range(a[2]):
        out = out+"C"
    for x in range(a[3]):
        out = out+"L"
    for x in range(a[4]):
        out = out+"X"
    for x in range(a[5]):
        out = out+"V"
    for x in range(a[6]):
        out = out+"I"
    return out

# Normalizes L-tuple values to standard
def normalizeLTup(a):
    while (a[6]>4):
        a[6] -= 5
        a[5] += 1
    while (a[6]<0):
        a[6] += 5
        a[5] -= 1
    while (a[5]>1):
        a[5] -= 2
        a[4] += 1
    while (a[5]<0):
        a[5] += 2
        a[4] -= 1
    while (a[4]>4):
        a[4] -= 5
        a[3] += 1
    while (a[4]<0):
        a[4] += 5
        a[3] -= 1
    while (a[3]>1):
        a[3] -= 2
        a[2] += 1
    while (a[3]<0):
        a[3] += 2
        a[2] -= 1
    while (a[2]>4):
        a[2] -= 5
        a[1] += 1
    while (a[2]<0):
        a[2] += 5
        a[1] -= 1
    while (a[1]>1):
        a[1] -= 2
        a[0] += 1
    return a

# helper function for numStrToData
def findLast(l):
    if l=="M":return 0
    elif l=="D":return 1
    elif l=="C":return 2
    elif l=="L":return 3
    elif l=="X":return 4
    elif l=="V":return 5
    elif l=="I":return 6
    else: return -1

def LNumToLTup(a):
    a = str(a)
    if a=="": return [0,0,0,0,0,0,0]
    k,last,result = 1,a[0],[0,0,0,0,0,0,0]
    for i in range(1,len(a)):
        if last==a[i]:k+=1
        else:
            result[findLast(last)] = k
            k=1
        last = a[i]
    result[findLast(last)] = k
    return result

def LNumAdd(a,b):
    adata,bdata = LNumToLTup(a),LNumToLTup(b)
    return LTupToLNum(normalizeLTup(map(add,adata,bdata)))
def LNumSub(a,b):
    adata,bdata = LNumToLTup(a),LNumToLTup(b)
    sdata = normalizeLTup(map(sub,adata,bdata))
    neg = reduce(or_,sdata)
    if neg < 0: return ''
    else: return LTupToLNum(sdata)

def HlfLTup(a):
    M = a[0]/2                         #1000/2=500
    D = a[1]/2 + 1*(a[0]%2)             #500 /2=250
    C = a[2]/2 + 2*(a[1]%2)             #100 /2=50
    L = a[3]/2 + 1*(a[1]%2) + 1*(a[2]%2) #50  /2=25
    X = a[4]/2 + 2*(a[3]%2)             #10  /2=5
    V = a[5]/2 + 1*(a[3]%2) + 1*(a[4]%2) #5   /2=2
    I = (a[6] + 5*(a[5]%2))/2
    return [M,D,C,L,X,V,I]

def DblLTup(a):
    d = [a[0]*2,a[1]*2,a[2]*2,a[3]*2,a[4]*2,a[5]*2,a[6]*2]
    return normalizeLTup(d)
def LTupAdd(a,b):
    return normalizeLTup(map(add,a,b))

def LTupHDMul(a,b):
    total = []
    while (a != [0,0,0,0,0,0,0]):
        if ((a[5]==0) and (a[6]%2==1)) or ((a[5]==1) and (a[6]%2==0)):
            total.append(b)
        a = HlfLTup(a)
        b = DblLTup(b)
    return reduce(LTupAdd,total)

def LNumMul(a,b):
    adata,bdata = LNumToLTup(a),LNumToLTup(b)
    return LTupToLNum(normalizeLTup(LTupHDMul(adata,bdata)))
