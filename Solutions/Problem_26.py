from math import *
from time import *

def primecheck(x):
    if x == 1:
        return False
    for i in range(2,floor(sqrt(x))+1):
        if x%i == 0:
            return False
    return True

def cycle_len(x):
    i=1
    m = (1000%x)*1000
    while m!=1000:
        m=(m%x)*10
        i +=1
    return i+2

t1=time()
prime_list = [i for i in range(101,1000,2) if primecheck(i)]
current = None
high = 0
for prime in prime_list:
    current = cycle_len(prime)
    if current > high:
        high = current
        answer = prime
print(f'Highest length is {high} of {answer},\nTime taken is {time()-t1}s')
