from math import gcd,sqrt
from time import time


t1=time()
l=1_500_000
# sides: c=m^2+n^2,a=m^2-n^2,b=2mn
# perimeter = 2m^2+2mn = 2m(m+n)
# m^2+n^2<l,m>n  => m<sqrt(l/2)
perimeter_set=set()
to_remove=set()
for m in range(2,int(sqrt(l/2))+1): 
    for n in range(1,m):
        if gcd(m,n)==1 and (m+n)%2==1:
            perimeter=2*m*(m+n)
            i=1
            new_per = perimeter
            while new_per<=l:
                if new_per in perimeter_set:
                    to_remove.add(new_per)
                else:
                    perimeter_set.add(new_per)
                new_per += perimeter
ans_set = perimeter_set.difference(to_remove)
print(len(ans_set))
print(f'Process completed in {time()-t1}s')