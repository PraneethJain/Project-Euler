from prime import factors
from time import time

t1 = time()
i = 1
while True:
    num = i * (i + 1) / 2
    if len(factors(num)) > 500:
        print(num)
        print(f"Process completed in {time()-t1}s")
        raise SystemExit
    i += 1
