from itertools import cycle
from time import time


t1 = time()
convergents = [2, 1]
k = 1
for i in cycle([1, 0, 0]):
    if i == 1:
        convergents.append(2 * k)
        k += 1
    if i == 0:
        convergents.append(1)
    if len(convergents) == 100:
        break
numerators = [2, 3]
for i in range(2, 100):
    numerators.append(numerators[i - 2] + convergents[i] * numerators[i - 1])
print(sum(list(map(int, list(str(numerators[99]))))))
print(f"Process completed in {time()-t1}s")
