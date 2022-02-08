from time import time

t1=time()
for a in range(1,1000):
    b = 500-a/2-(a**2)/(2*(1000-a))
    if b>0 and b==int(b):
        c = (a**2)/(2*(1000-a))+500-a/2
        if c>0 and c==int(c):
            print(int(a*b*c))
            print(f'Process completed in {time()-t1}s')
            raise SystemExit