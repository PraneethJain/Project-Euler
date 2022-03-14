from prime import primecheck, primelist
from rich import print
from time import time

t1 = time()
ans_set = set()
N = 50_000_000
primes = primelist(int(N**0.5))
for prime4 in primes:
    fourthed = prime4**4
    if fourthed > N:
        break
    for prime3 in primes:
        cubed = prime3**3
        if fourthed + cubed > N:
            break
        for prime2 in primes:
            squared = prime2**2
            num = fourthed + cubed + squared
            if num > N:
                break
            else:
                ans_set.add(num)

print(len(ans_set))
print(f"Process completed in {time()-t1} seconds")
