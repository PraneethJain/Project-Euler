from time import time

t1=time()
sum=0
for i in range(1,10**6):
    if str(i)==str(i)[::-1] and bin(i)[2:]==bin(i)[2:][::-1]:
        sum += i
print(sum)
print(f'Process completed in {time()-t1}')