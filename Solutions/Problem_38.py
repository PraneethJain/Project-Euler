from time import time

t1=time()
high = 1
for i in range(1,100000):
    j=1
    num_str=''
    while len(num_str)<9:
        num_str += str(i*j)
        j += 1
    if len(set(num_str))==9 and len(num_str)==9 and '0' not in num_str:
        current = int(num_str)
        if current>high:
            high = current
print(high)
print(f'Process completed in {time()-t1}s')