from time import time

t1 = time()
current = None
high = 0
for a in range(1, 100):
    for b in range(1, 100):
        current = sum(list(map(int, list(str((a**b))))))
        if current > high:
            high = current
print(high)
print(f"Process completed in {time()-t1}s")
