import math
import time


def LCM(x,y):
    return(int((x*y)/(math.gcd(x,y))))

t1= time.time()
ans = 1
for i in range(1,20):
    ans = LCM(ans,i)
print(ans,time.time()-t1)
input('Press ENTER to exit')
