##To find the nth prime number

n = int(input("Enter the prime number number: "))
prime = [2,3]
i=3
if 0<n<3:
    print(prime[n-1])
elif n>2:
    while True:
        i+=1
        status=True
        for j in range(2,int(i/2)+1):
            if (i%j==0):
                status = False
                break
        if(status==True):
            prime.append(i)
        if(len(prime)==n):
            break
    print(prime[n-1])
else:
    print("Bad Input")
input('Press ENTER to exit')
