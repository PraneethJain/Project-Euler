import math
import time
def primecheck(x):
    if x >= 2:
        for i in range(2,math.floor(math.sqrt(x)+1)):
            if x%i==0:
                return False
        return True
    else:
        return False
t1 = time.time()
high = 0
aans=None
baans=None
for a in range(-999,1000):
    for b in range(-1000,1001):
        n=0
        current = 0
        if pow(n,2)+a*n+b>0:
            while primecheck(pow(n,2)+a*n+b) is True:
                current += 1
                n += 1
            if current > high:
                high = current
                aans=a
                baans=b
print(aans*baans,time.time()-t1)

