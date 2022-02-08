from time import time
from itertools import product

t1=time()
L=set()
for a,b in product(range(2,101),repeat=2):
    L.add(a**b)
print(len(L))
print(f'Process completed in {time()-t1}s')