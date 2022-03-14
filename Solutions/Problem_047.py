from time import time
from sympy.ntheory import factorint

t1 = time()
i = 1
while True:
    if all(len(factorint(j)) == 4 for j in range(i, i + 4)):
        print(i)
        print(f"Process completed in {time()-t1}s")
        break
    i += 1
