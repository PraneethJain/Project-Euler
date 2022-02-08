import time
t1 = time.time()
print(sum(int(i) for i in list(str(2**1000))),time.time()-t1)