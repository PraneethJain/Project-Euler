from prime import factors
from time import time


def abundant(x):
    return sum(factors(x))>2*x

t1 = time()
abundant_numbers=[i for i in range(12,28124) if abundant(i)]
can_sum=set()
for i in abundant_numbers:
    for j in abundant_numbers:
        if i+j>28123:
            break
        else:
            can_sum.add(i+j)

print(int(28123*28124/2)-sum(can_sum))
print(f'Process completed in {time()-t1}s')
