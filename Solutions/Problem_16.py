from time import time
t1 = time()
print(sum(int(i) for i in list(str(2**1000))))
print(f'Process completed in {time()-t1}s')