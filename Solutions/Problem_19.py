from time import time
t1 = time()
dic = {'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
ans=0
num=2 # 1 Jan 1901 was a Tuesday
for year in range(1901,2001):
    for month in dic:
        num += dic[month]
        if month == 'February' and year % 4 == 0:
            num += 1
        if num % 7 == 0:
            ans += 1
print(ans)
print(f'Process completed in {time()-t1}s')