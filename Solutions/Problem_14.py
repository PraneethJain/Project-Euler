import time
def collatz(x):
    length = 1
    while x!=1:
        if x%2==0:
            x=x/2
            length += 1
        elif x%2==1:
            x=(3*x+1)/2
            length += 2
    return length


t1 = time.time()
best=1
for i in range(2,1000001):
    now = collatz(i)
    if now>best:
        best=now
        answer = i
print(answer,time.time()-t1)