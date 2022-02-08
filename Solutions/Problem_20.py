from math import factorial as f
from time import time
t1 = time()
print(sum(int(i) for i in list(str(f(100)))))
print(f'Process completed in {time()-t1}s')
