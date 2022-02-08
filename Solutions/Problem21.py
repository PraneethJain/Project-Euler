from prime import factors
from time import time

def d(n):
    return sum(factors(n))-n

t1=time()
L=set()
for a in range(2,10**4):
    b=d(a)
    if b!=a and d(b)==a:
        L.add(a)
        L.add(b)

print(sum(L))
print(f'Process completed in {time()-t1}s')