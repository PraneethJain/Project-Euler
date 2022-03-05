# axb grid ==> (a+1) vertical lines, (b+1) horizontal lines
# choose any two vertical lines and any two horizontal lines
# (a+1)c2 * (b+1)c2 =  number of rectangles in axb grid!

from time import time
from rich import print
from math import factorial as f
from itertools import product


def c(n, r):
    return f(n) / (f(r) * f(n - r))


t1 = time()
ans_a, ans_b = 0, 0
min_diff = 100000
for a, b in product(range(10, 100), repeat=2):
    diff = abs(2_000_000 - c(a + 1, 2) * c(b + 1, 2))
    if diff < min_diff:
        ans_a = a
        ans_b = b

print(ans_a * ans_b)
print(f"Process completed in {time()-t1} seconds")
