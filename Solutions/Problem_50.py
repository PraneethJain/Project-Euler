from prime import primelist
from time import time as t


t1 = t()
numofprimes = 0
num_of_primes = []
primes = []
prime_list = primelist(10**6)
for i, _ in enumerate(prime_list):
    for j in range(i + numofprimes, len(prime_list)):
        maybe_prime = sum(prime_list[i:j])
        if maybe_prime < 10**6:
            if maybe_prime in prime_list:
                numofprimes = j - i
                primes.append(maybe_prime)
                num_of_primes.append(numofprimes)
        else:
            break
print(primes[num_of_primes.index(max(num_of_primes))])
print(f"Process completeted in {t()-t1}s")
