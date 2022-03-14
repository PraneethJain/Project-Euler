from sympy.ntheory import totient
from time import time

t1 = time()
ans = 0
for i in range(2, 10**6 + 1):
    ans += totient(i)
print(ans)
print(f"Process completed in {time()-t1}s")
# Completed in 51.907002210617065s
