# 10^n is n+1 digits so base can only be [1,9]
from time import time

t1=time()
ans=0
for a in range(1,10):
    for b in range(1,100):
        if b==len(str(a**b)):
            ans+=1
print(ans)
print(f'Process completed in {time()-t1}s')
