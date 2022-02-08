from itertools import permutations
from prime import primelist
from time import time


t1=time()
prime_list=primelist(18)
permutated = list(permutations('0123456789'))

num_list=[''.join(element) for element in permutated]
ans = 0

for num in num_list:
    if len(num)==10:
        if all(int(num[i:i+3])%prime_list[i-1]==0 for i in range(1,8)):
                ans += int(num)

print(ans)
print(f'Process completed in {time()-t1}s')
