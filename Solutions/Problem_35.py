from prime import primecheck
from itertools import permutations as p
from time import time


def rotations(x):
    rotations=set()
    for i in range(len(str(x))):
        rotations.add(int(str(x)[i:]+str(x)[:i]))
    return rotations


t1=time()
circular= []
primelist = set([i for i in range(2,1000000) if primecheck(i)])
for prime in primelist:
    L=list(p(str(prime)))
    permuted = rotations(prime)
    if permuted.issubset(primelist):
        circular.append(prime)
print(len(set(circular)))
print(f'Process completed in {time()-t1}s')
