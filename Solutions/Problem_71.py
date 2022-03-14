from time import time

t1 = time()
x = 10**6
while x % 7 != 0:
    x = x - x % 7
print(int(3 * x / 7 - 1))
print(f"Process completed in {(time()-t1)}s")
