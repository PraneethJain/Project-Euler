import math
import time


def abundant(x):
    ans = []
    for i in range(1,math.floor(math.sqrt(x))+1):
        if x % i == 0:
            ans.append(i)
            if i !=1:
                ans.append(int(x/i))
    if sum(set(ans)) > x:
        return True
    else:
        return False

t1 = time.time()
abundant_numbers=[i for i in range(12,28124) if abundant(i)]
can_sum=set()
for i in abundant_numbers:
    for j in abundant_numbers:
        if i+j>28123:
            break
        else:
            can_sum.add(i+j)
cant_sum=[i for i in range(1,28124) if i not in can_sum]
print(cant_sum)
print(sum(cant_sum),time.time()-t1)
