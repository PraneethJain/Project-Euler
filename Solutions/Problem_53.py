from math import factorial as f
from time import time

def ncr(n,r):
    return int(f(n)/(f(r)*f(n-r)))

t1=time()
ans = 0
for n in range(1,101):
    for r in range(0,n+1):
        if ncr(n,r)>10**6:
            ans +=1
print(ans)
print(f'Process completed in {time()-t1}s')