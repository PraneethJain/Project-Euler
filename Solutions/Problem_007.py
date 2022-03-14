from prime import primelist
from time import time

t1 = time()
print(primelist(200000)[10000])
print(f"Process completed in {time()-t1}s")
