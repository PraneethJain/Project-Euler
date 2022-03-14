from fractions import Fraction as f
from time import time


t1 = time()
L = set()
for den in range(1, 12001):
    for num in range(1, den):
        if 1 / 3 < num / den < 0.5:
            L.add(f(num, den))
        elif num / den > 0.5:
            break
print(len(L))
print(f"Process completed in {time()-t1}s")
# Completed in 56.8684720993042s
