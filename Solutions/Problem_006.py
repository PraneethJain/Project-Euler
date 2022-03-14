from time import time

t1 = time()
print((100 * (100 + 1) / 2) ** 2 - 100 * (100 + 1) * (2 * 100 + 1) / 6)
print(f"Process completed in {time()-t1}s")
