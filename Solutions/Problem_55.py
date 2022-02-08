from time import time

def palindrome_check(x: int) -> bool:
    return str(x)==str(x)[::-1]
def Lychrel_Check(x):
    num = x
    i=0
    while i<50:
        num = num + int(str(num)[::-1])
        if palindrome_check(num):
            return False
        i+=1
    if i==50:
        return True
    return False

t1=time()
print(len([i for i in range(1,10001) if Lychrel_Check(i)]))
print(f'Process completed in {time()-t1}s')