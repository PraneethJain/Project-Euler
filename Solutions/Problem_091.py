from itertools import product
from rich.progress import track
from rich import print
from time import time


def right_check(x1, y1, x2, y2):
    a = x1**2 + y1**2
    b = x2**2 + y2**2
    c = (x2 - x1) ** 2 + (y2 - y1) ** 2
    return (a + b == c) or (b + c == a) or (a + c == b)


t1 = time()
ans = 0
for x1, y1, x2, y2 in product(range(51), repeat=4):
    # Slope of one greater than other so that no repeated
    if x1 * y2 > y1 * x2 and right_check(x1, y1, x2, y2):
        ans += 1

print(ans)
print(f"Process completed in {time()-t1} seconds")
