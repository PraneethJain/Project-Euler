from time import time


def collatz(x):
    length = 1
    while x != 1:
        if x % 2 == 0:
            x = x / 2
            length += 1
        elif x % 2 == 1:
            x = (3 * x + 1) / 2
            length += 2
    return length


t1 = time()
high = 1
for i in range(500001, 1000001, 2):
    current = collatz(i)
    if current > high:
        high = current
        answer = i
print(answer)
print(f"Process completed in {time()-t1}s")
