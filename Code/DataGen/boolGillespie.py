import fileinput
import re
import random
import functools
import operator
from collections import Counter
import math
import json
from sys import stderr
import argparse

parser = argparse.ArgumentParser(description='Run the boolean Gillespie algorithm on the given influence system.')
parser.add_argument('file',
                    help='Input file describing the influence system')
parser.add_argument('h', type=int,
                    help='Precision parameter')
parser.add_argument('k', type=int,
                    help='Maximum size of the disjunctions')

class Indexer(dict):
    def __missing__(self,key):
        n = len(self)
        self[key] = n
        return n
cre = re.compile(r'([\w\*]+)')
cre2 = re.compile(r'(?P<reac>[^/]*)(/(?P<inhib>.*))?-(?P<kind>[> <])(?P<prod>[^(]*)(\((?P<prop>.*)\))?')
cre3 = re.compile(r'(?:(.*)\*)?(.*)')

indexer = Indexer()

args = parser.parse_args()
f = ""
with open(args.file) as foo:
    f = foo.read()

reactions = []

def specList(s):
    if not s:
        return []
    items = cre.findall(s)
    res = []
    for i in items:
        finalParse = cre3.match(i).groups()
        res.append(indexer[finalParse[1]])
    return res

lines = f.strip().split('\n')

for l in lines[1:]:
    reaction = {}
    mdic = cre2.match(l).groupdict()
    reaction['reactants'] = specList(mdic['reac'])
    reaction['products'] = specList(mdic['prod'])
    reaction['inhibitors'] = specList(mdic['inhib'])
    reaction['propensity'] = float(mdic['prop'] or 1)
    reaction['kind'] = mdic['kind']
    reactions.append(reaction)

state = [False]*len(indexer)
dicState = json.loads(lines[0])
for (k,v) in dicState.items():
    state[indexer[k]] = (v > 0)

def canFire(r):
    for spec in r['reactants']:
        if not state[spec]:
            return False
    for spec in r['inhibitors']:
        if not state[spec]:
            return True
    return not r['inhibitors']

def bigL(h,k):
    return int(2*h*((2*len(indexer))**(k+1)+math.log(h))+1)


influences = []
for _ in indexer:
    influences.append(set())
    influences.append(set())


h = args.h
k = args.k
loop_end = bigL(h,k)
for loop_n in range(loop_end):
    if loop_n % (2)**16 == 0:
        print(state,file=stderr)
        for (k,v) in indexer.items():
            if state[v]:
                print(k,end=' ',file=stderr)
        print(file=stderr)
        print(100*loop_n/loop_end,file=stderr)

    doable = [r for r in reactions if canFire(r)]
    if not doable:
        break
    chosen = random.choices(doable,[r['propensity'] for r in doable])[0]
    activated = chosen['kind'] == '>'
    for r in chosen['products']:
        if state[r] ^ activated:
            if activated:
                influences[2*r] |= {tuple([2*i + (1 if x else 0) for (i,x) in enumerate(state)])}
            else:
                influences[2*r+1] |= {tuple([2*i + (1 if x else 0) for (i,x) in enumerate(state)])}
        state[r] = activated


result = {'indexer': indexer, 'influences': [list(x) for x in influences]}

print(json.dumps(result))
