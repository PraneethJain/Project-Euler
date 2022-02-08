from math import sqrt
from time import time


def period(x): # https://en.wikipedia.org/wiki/Periodic_continued_fraction
    if square_check(x):
        return 0
    else:
        ans=0
        m=0
        d=1
        a=int(sqrt(x))
        while a!=2*int(sqrt(x)):
            m=d*a-m
            d=(x-m**2)/d
            a=int((sqrt(x)+m)/d)
            ans+=1
        return ans
def square_check(x):
    return (int(x**0.5))**2==x

t1=time()
ans=0
for i in range(1,10**4):
    if period(i)%2==1:
        ans+=1
print(ans)
print(f'Process completed in {time()-t1}s')