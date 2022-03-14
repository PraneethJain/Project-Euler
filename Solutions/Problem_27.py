from time import time
from prime import primecheck

t1 = time()
high = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        if n**2 + a * n + b > 0:
            while primecheck(pow(n, 2) + a * n + b):
                n += 1
            if n > high:
                high = n
                aans = a
                baans = b
print(aans * baans)
print(f"Process completed in {time()-t1}s")
