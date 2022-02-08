from time import time

t1=time()
fib = [1,1]
i=0
while fib[-1]<4*(10**6):
    fib.append(fib[i]+fib[i+1])
    i+=1
fib_even=[i for i in fib if i%2==0]
print(sum(fib_even))
print(f'Process completed in {time()-t1}s')