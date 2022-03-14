from sympy.ntheory import factorint
from time import time

t1 = time()
print(max(factorint(600851475143)))
print(f"Process completed in {time()-t1}s")
