from math import factorial as f
from time import time
t1=time()
print(int(f(40)/(f(20)**2)))
print(f'Process completed in {time()-t1}s')