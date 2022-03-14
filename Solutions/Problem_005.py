from math import gcd
from time import time


def LCM(x, y):
    return int((x * y) / (gcd(x, y)))


t1 = time()
ans = 1
for i in range(1, 20):
    ans = LCM(ans, i)
print(ans)
print(f"Process completed in {time()-t1}s")
