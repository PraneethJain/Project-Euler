from prime import primelist, primecheck
from time import time


t1 = time()
temp = primelist(10**6)
prime_list = [prime for prime in temp if prime > 10**4]
digit_list = [str(i) for i in range(10)]
all_digit_list = []
for p in prime_list:
    prime = str(p)
    repeated3 = list(set([digit for digit in digit_list if prime.count(digit) == 3]))
    repeated5 = list(set([digit for digit in digit_list if prime.count(digit) == 5]))
    if len(repeated5) == 1:
        all_digit_list.append(prime.replace(repeated5[0], "*"))
    if len(repeated3) == 1:
        all_digit_list.append(prime.replace(repeated3[0], "*"))

for ele in all_digit_list:
    L = []
    for i in range(10):
        num = ele.replace("*", str(i))
        num = int(num)
        if primecheck(num):
            L.append(num)
    if len(L) == 8 and len(str(L[0])) == len(str(L[1])):
        print(min(L))
        print(f"Process completed in {time()-t1}s")
        raise SystemExit
