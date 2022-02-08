from time import time

t1=time()
L=set()
for i in range(0,99):
    for j in range(100,9999):
        k=str(i)+str(j)+str(i*j)
        if len(k)==9 and set(k)==set('123456789'):
            L.add(i*j)
print(sum(L))
print(f'Process completed in {time()-t1}s')