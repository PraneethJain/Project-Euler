import time
t1 = time.time()
print(sum(i for i in range(2,5*(9**5)) if i == sum(int(j)**5 for j in list(str(i)))),time.time()-t1)