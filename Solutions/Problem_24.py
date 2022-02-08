from itertools import permutations
from time import time
t1=time()
print(''.join(list(permutations('0123456789'))[999999]))
print(f'Process completed in {time()-t1}s')