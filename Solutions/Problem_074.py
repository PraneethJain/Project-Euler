from time import time
from rich import print
from rich.progress import track

f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def sum_fac(x):
    return sum(f[int(i)] for i in str(x))


t1 = time()
ans = 0
dic = {}
for num in track(range(10**6), description="[bold cyan]Processing[/bold cyan]"):
    L = [num]
    i = 0
    while sum_fac(L[-1]) not in L:
        if L[-1] in dic:
            temp = dic[L[-1]][1:]
            L.extend(temp)
            break
        L.append(sum_fac(L[i]))
        i += 1
    dic[num] = L
    if len(L) == 60:
        ans += 1
print(ans)
print(f"Process completed in {time()-t1}s")
