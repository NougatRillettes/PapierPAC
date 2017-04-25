from copy import copy
from collections import deque
import json
from itertools import combinations
import argparse
from sys import stderr

parser = argparse.ArgumentParser(description='Run PAC learning for k-CNF on one of \
                                                the simulators output.')
parser.add_argument('file',
                    help='Input file containing examples')
parser.add_argument('k',type=int,
                    help='Maximum size of the disjunctions')
parser.add_argument('--hints',action='store',\
                    default="")





class Partition:
    def __init__(self):
        self.marked = False
        self.elems = []
        self.code = 0
        self.children = []
        self.parents = []

    def __repr__(self):
        return "(" + repr(self.elems) + " | " + repr(self.code) + " | " + repr(self.marked) +  ")"

def generate_k_partitions(k,n):
    table = {0:Partition()}
    current_gen = [table[0]]
    for _ in range(k):
        new_gen = []
        for x in current_gen:
            for i in range (2*n):
                if 2**i & x.code == 0:
                    code = x.code | (2**i)
                    if not code in table:
                        table[code] = Partition()
                        table[code].elems = copy(x.elems)
                        table[code].elems.append(i)
                        table[code].code = code
                        new_gen.append(table[code])
                    table[code].parents.append(x)
                    x.children.append(table[code])
            current_gen = new_gen
    return table

def code_of(l):
    return sum([2**i for i in l])

def mark_all_greater(code,table):
    stack = deque([table[code]])
    while stack:
        x = stack.pop()
        if not x.marked:
            x.marked = True
            stack.extend(x.parents)

def sample(l,table,k):
    samples = combinations(l,k) if len(l) >= k else [l]
    for s in samples:
        code = code_of(s)
        mark_all_greater(code,table)

def conjonc(table,n):
    res = []
    stack = deque(table[0].children)
    while stack:
        x = stack.popleft()
        stack.extend(x.children)
        if not x.marked:
            tauto = False
            for i in range(n):
                extract1 = bool((4**i)*2 & x.code)
                extract2 = bool((4**i) & x.code)
                tauto = extract2 and extract1
                #print(x.elems,extract1,extract2,tauto)
                if tauto:
                    break
            if not tauto:
                res.append(x.elems)
            sub_stack = deque(x.children)
            while sub_stack:
                y = sub_stack.pop()
                if not y.marked:
                    y.marked = True
                    sub_stack.extend(y.children)
            x.marked = True
    return res

args = parser.parse_args()

dic = None
with open(args.file) as f:
    dic = json.loads(f.read())

indexer = dic['indexer']
influences = dic['influences']
n = len(indexer)
revIndexer = [None]*n
for (k,v) in indexer.items():
    revIndexer[v] = k

def varName(i):
    if i % 2 == 0:
        return revIndexer[i//2]
    else:
        return '!'+revIndexer[i//2]

hints = {}
if args.hints:
    with open(args.hints) as f:
        hints = json.loads(f.read())

k = args.k


def applyAlg(i):
    table = generate_k_partitions(k,n)
    #print(table)
    for s in influences[i]:
        s2 = set(s)
        try:
            #s2 = [x for x in s if revIndexer[x//2] in hints[revIndexer[i]]]
            s2 |= {2*j for j in range(n) if revIndexer[j] not in hints[revIndexer[i//2]]}
            s2 |= {2*j+1 for j in range(n) if revIndexer[j] not in hints[revIndexer[i//2]]}
            #print([varName(x) for x in s],[varName(x) for x in s2],sep='\n',file=stderr,end='--\n')
        except KeyError:
            pass
        sample(s2,table,k)
    print("{}{} : ".format(revIndexer[i//2], '-' if i%2 else '+'),end='')
    if not table[0].marked: #Never sampled, hence false
        print("False")
        return
    firstC = True
    for c in conjonc(table,n):
        if not firstC:
            print(" /\ ",end='')
        firstC = False
        if len(c) == 1:
            print(varName(c[0]),end='')
        else:
            print('(',end='')
            firstT = True
            for t in c:
                if not firstT:
                    print(' \/ ',end='')
                firstT = False
                print(varName(t),end= '')
            print(' )',end='')
    if firstC:
        print("True",end='')
    print()


for i in range(n):
    applyAlg(2*i)
    applyAlg(2*i+1)
