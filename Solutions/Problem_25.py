import time


def fibonacci(n): #(Found cool way to write Fibonacci from net)
    a=1
    b=0
    while n>1:
        a,b=a+b,a
        n=n-1
    return a

t1 = time.time()
i=1
x=1
while x != 1000:
    i+=1
    x=len(str(fibonacci(i)))
    print(x)
print(i,time.time()-t1)