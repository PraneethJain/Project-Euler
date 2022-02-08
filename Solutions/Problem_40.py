num_str='0'
for i in range(1,10**6+1):
    num_str += str(i)
ans=1
for i in range(7):
    ans*=int(num_str[10**i])
print(ans)
