import math
import time


def factors(x):
    ans = []
    for i in range(1,math.floor(math.sqrt(x)+1)):
        if x % i == 0:
            ans.append(i)
            ans.append(int(x/i))
    return(len(set(ans)))

t1 = time.time()
i=1000
while factors(i*(i+1)/2)<=500:
    i+=1
print(int(i*(i+1)/2),time.time()-t1)