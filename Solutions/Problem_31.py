from time import time

t1=time()
ans=0
for a1 in range(0,201,1):
    for a2 in range(0,201-a1,2):
        for a5 in range(0,201-a1-a2,5):
            for a10 in range(0,201-a1-a2-a5,10):
                for a20 in range(0,201-a1-a2-a5-a10,20):
                    for a50 in range(0,201-a1-a2-a5-a10-a20,50):
                        for a100 in range(0,201-a1-a2-a5-a10-a20-a50,100):
                            for a200 in range(0,201-a1-a2-a5-a10-a20-a50-a100,200):
                                if a1+a2+a5+a10+a20+a50+a100+a200==200:
                                    ans+=1
print(ans)
print(f'Process completed in {time()-t1}s') #what