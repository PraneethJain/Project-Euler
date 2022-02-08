def convert(x):
    if x!=1:
        binary=''
        while x!=1:
            binary = binary + str(x%2)
            x=x//2
        return (binary + '1')[::-1]
    return '1'


sum=0
for i in range(1,1_000_000):
    if str(i)==str(i)[::-1] and convert(i)==convert(i)[::-1]:
        sum += i
print(sum)
