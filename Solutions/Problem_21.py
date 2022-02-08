import math
import time


def factors(x):
    ans = []
    for i in range(1,math.floor(math.sqrt(x))+1):
        if x % i == 0:
            ans.append(i)
            if i !=1:
                ans.append(int(x/i))
    return sum(set(ans))


t1 = time.time()
final =[]
dic = {i:0 for i in range(0,10000)}
for i in range(0,10000):
    dic[i]=factors(i)
for i in range(0,10000):
    for j in range(0,10000):
            if i == dic[j] and dic[i] == j and i!=j :
                final.append(i)
                final.append(j)
print(set(final))
print(sum(set(final)),time.time()-t1)