from sympy import partition as p
from time import time
from rich import print

t1 = time()
n = 10000
while p(n) % 1_000_000 != 0:
    n += 1

print(n)
print(f"Process completed in {time()-t1}s")
