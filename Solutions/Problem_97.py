from rich import print
from time import time

t1 = time()
print(((2**7830457) * 28433 + 1) % (10**10))
print(f"Process completed in {time()-t1} seconds")
