from prime import factors
from time import time


def sigma(n: int) -> int:
    """Returns sum of proper factors of n"""
    return sum(factors(n))

dic = {0:1,1:1}
def p(n: int) -> int:
    """Returns number of partitions of n"""
    sum=0
    for k in range(n):
        try:
            sum+=(sigma(n-k)*dic[k])
        except:
            sum+=(sigma(n-k)*p(k))
    dic[n]=int(sum/n)
    return int(sum/n)

t1=time()
print(p(100)-1) # Does not include 100 as a partition, so -1
print(f'Process completed in {time()-t1}s')
