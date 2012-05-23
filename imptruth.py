def LTruthToBool(a):
    if a == 'VERUS':
        return 1
    elif a == 'FALSUS':
        return 0
    else:
        return 1

def LTruthNot(a,b):
    if a == 'VERUS':
        return 'FALSUS'
    elif a == 'FALSUS':
        return 'VERUS'
    else:
        return 'NON VERITAS'

def LTruthAnd(a,b):
    at,bt = LTruthToBool(a),LTruthToBool(b)
    if at and bt:
        return 'VERUS'
    else:
        return 'FALSUS'

def LTruthOr(a,b):
    at,bt = LTruthToBool(a),LTruthToBool(b)
    if at or bt:
        return 'VERUS'
    else:
        return 'FALSUS'

def LTruthXor(a,b):
    at,bt = LTruthToBool(a),LTruthToBool(b)
    if at != bt:
        return 'VERUS'
    else:
        return 'FALSUS'
