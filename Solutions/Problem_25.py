from time import time

t1 = time()
fib = [1, 1]
i = 0
while len(str(fib[-1])) < 1000:
    fib.append(fib[i] + fib[i + 1])
    i += 1
print(len(fib))
print(f"Process completed in {time()-t1}s")
