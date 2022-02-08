import time
t1=time.time()
L=[]
for a in range(2,101):
    for b in range(2,101):
        L.append(pow(a,b))
print(len(set(L)),time.time()-t1)