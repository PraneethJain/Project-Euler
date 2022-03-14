from prime import primelist
from time import time

t1 = time()
print(sum(primelist(2 * 10**6)))
print(f"Process completed in {time()-t1}s")
