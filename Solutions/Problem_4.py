from time import time
t1 = time()

high=0
for i in range(100,1000):
    for j in range(100,1000):
        high=i*j if str(i*j)==str(i*j)[::-1] and i*j>high else high
            
print(high)
print(f'Process completed in {time()-t1}s')