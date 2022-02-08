import time
t1 = time.time()
all = []
palindrome=[]
for i in range(100,1000):
    for j in range(100,1000):
        all.append(i*j)
for i in all:
    if str(i)==str(i)[::-1]:
        palindrome.append(i)
print(max(palindrome),time.time()-t1)