# x(x-1)/(y(y-1))=1/2
# 2(x^2-x)=(y^2-y)
# OEIS A011900

from rich import print
from time import time
from math import sqrt

t1 = time()
cache = [1, 3]
total = 0
while total < 10**12:
    x = 6 * cache[-1] - cache[-2] - 2
    cache.append(x)
    total = (1 + sqrt(1 + 8 * (x**2 - x))) / 2

print(x)
print(f"Process completed in {time()-t1} seconds")
