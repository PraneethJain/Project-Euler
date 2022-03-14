from math import sqrt
from time import time
from prime import primelist
from itertools import product


t1 = time()
a = int(sqrt(10**7))
prime_list = primelist(2 * a)
low = 10
ans = 0
for p1, p2 in product(prime_list, repeat=2):
    if p1 > p2:
        phi = (p1 - 1) * (p2 - 1)
        n = p1 * p2
        if p1 * p2 <= 10**7 and sorted(list(str(n))) == sorted(list(str(phi))):
            current = n / phi
            if current < low:
                low = current
                ans = (n, p1, p2, low)
print(f"Answer is {ans[0]}\n{ans[0]}={ans[1]}*{ans[2]} and ratio is {ans[3]}")
print(f"Process completed in {time()-t1}s")
