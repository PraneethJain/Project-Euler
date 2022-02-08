from time import time


t1 = time()
p_list=[]
from math import sqrt
for a in range(1,500):
    for b in range(1,500):
        c = sqrt(a**2+b**2)
        if c%1==0 and a+b+c<=1000:
            p_list.append(a+b+c)
current = None
high = 0
for p in p_list:
    current = p_list.count(p)
    if current>high:
        high = current
        ans = p
print(f'p={int(ans)} has {high} solutions')
print(f'Process completed in {time()-t1}s')