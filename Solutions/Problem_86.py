# draw the net
# if a>=b>=c shortest length is a^2+(b+c)^2
# instead of iterating both b and c, directly iterate bplusc
# when b+c<a: b=bplusc-1,bplusc-2,...,bplusc-bplusc/2, so floor(bplusc/2) solutions
# when b+c>a: b=bplusc/2,bplusc./+1,bplusc/2+2,...,a so (a-ceil(bplusc/2)+1) solutions

from fraction import square_check
from rich import print
from rich.progress import track
from time import time
from math import floor, ceil

t1 = time()
ans = 0
M = 2
while ans < 1_000_000:
    M += 1
    for bplusc in range(3, 2 * M):
        if square_check(M**2 + bplusc**2):
            if bplusc <= M:
                ans += floor(bplusc / 2)
            else:
                ans += M - ceil(bplusc / 2) + 1

print(M)
print(f"Process completed in {time()-t1} seconds")
