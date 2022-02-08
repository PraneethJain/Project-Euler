import math
from itertools import permutations as p


def primecheck(x):
    for i in range(2,math.floor(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def rotations(x):
    rotations=set()
    for i in range(len(str(x))):
        rotations.add(int(str(x)[i:]+str(x)[:i]))
    return rotations


circular= []
primelist = set([i for i in range(2,1000000) if primecheck(i)])
for prime in primelist:
    L=list(p(str(prime)))
    permuted = rotations(prime)
    if permuted.issubset(primelist):
        circular.append(prime)
print(len(set(circular)))
