from rich import print
from rich.progress import track
from time import time


def next(x):
    return sum(i**2 for i in list(map(int, list(str(x)))))


dic = {1: False, 89: True}


def reach_89(x):
    original = x
    while True:
        try:
            dic[original] = dic[x]
            return dic[x]
        except:
            if x == 1:
                dic[original] = False
                return False
            if x == 89:
                dic[original] = True
                return True
            x = next(x)


t1 = time()
ans = 0
for i in track(range(1, 10_000_000), "Processing"):
    if reach_89(i):
        ans += 1

print(ans)
print(f"Process completed in {time()-t1} seconds")
