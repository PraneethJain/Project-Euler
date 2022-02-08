from math import factorial as f
from time import time

t1=time()
ans=0
for x in range(10,10**6):
    if sum(f(int(i)) for i in str(x))==x:
        ans+=x
print(ans)
print(f'Process completed in {time()-t1}s')