from fractions import Fraction as f
from time import time
from math import prod

t1=time()
L=set()
for den in range(10,100):
    for num in range(10,den):
        if den%11 != 0 and num%11 !=0 and str(num)[1]==str(den)[0]:
            try:
                if f(num,den)==f(int(str(num)[0]),int(str(den)[1])):
                    L.add(f(num,den))
            except:
                pass

print(prod(L))
print(f'Process completed in {time()-t1}s')