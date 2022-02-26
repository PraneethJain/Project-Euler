from time import time

t1 = time()
print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))
print(f"Process completeed in {time()-t1}s")
