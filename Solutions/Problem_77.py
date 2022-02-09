from prime import factors,primecheck
from time import time


def sum_prime(x: int) -> int:
    """Returns sum of prime factors of x"""
    return sum(i for i in factors(x) if primecheck(i))

dic = {1:0}
def r(n: int) -> int:
    """Returns number of prime partitions of n"""
    if n==1:
        return 0
    sum = sum_prime(n)
    for j in range(1,n):
        try:
            sum += sum_prime(j)*dic[n-j]
        except:
            sum += sum_prime(j)*r(n-j)
    dic[n]=int(sum/n)
    return int(sum/n)

t1=time()
n=1
while r(n)<5000:
    n+=1
print(n)
print(f'Process completed in {time()-t1}s')