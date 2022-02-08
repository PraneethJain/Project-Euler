from time import time
t1=time()
print([x for x in range(1,10**6) if all(set(str(i*x))==set(str(x)) and len(str(i*x))==len(str(x)) for i in range(2,7))][0])
print(f'Process completed in {time()-t1}s')