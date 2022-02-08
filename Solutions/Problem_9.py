def tripletcheck(x,y,z):
    if x**2+y**2==z**2:
        return(True)
    else:
        return(False)


for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            if i+j+k==1000:
                if tripletcheck(i,j,k):
                    print(i,j,k)
input('Press ENTER to exit')
