from time import time

t1 = time()
print(sum([(i**i) % (10**10) for i in range(1, 1001)]) % (10**10))
print(f"Process completed in {time()-t1}s")
