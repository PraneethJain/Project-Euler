from math import *
from time import time
from prime import primecheck


def cycle_len(x):
    i = 1
    m = (1000 % x) * 1000
    while m != 1000:
        m = (m % x) * 10
        i += 1
    return i + 2


t1 = time()
prime_list = [i for i in range(101, 1000, 2) if primecheck(i)]
current = None
high = 0
for prime in prime_list:
    current = cycle_len(prime)
    if current > high:
        high = current
        answer = prime
print(f"Highest length is {high} of {answer}")
print(f"Process completed in {time()-t1}s")
