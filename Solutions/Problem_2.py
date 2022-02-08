import math

x = int(input("Enter the upper limit: "))
list = [1,2]
for i in range(2,100000000):
    if list[i-1]<x:
        list.append(list[i-1]+list[i-2])
    else:
        list.pop(i-1)
        break
for x in list:
    if x%2!=0:
        list.remove(x)
print(list)
sum = 0
for i in range(0,math.ceil(len(list)/2)):
    sum = sum + list[2*i]
print(sum)
input('Press ENTER to exit')
