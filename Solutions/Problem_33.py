from math import gcd
numerator=1
denominator=1
for i in range(10,100):
    for j in range(i+1,100):
        if i%10==0 and j%10==0:
            continue
        elif i%11==0 and j%11==0:
            continue
        else:
            if int(str(j)[1]) != 0:
                if int(str(i)[1])==int(str(j)[0]):
                    if i/j==int(str(i)[0])/int(str(j)[1]):
                            numerator *= i
                            denominator *= j
print(denominator//gcd(numerator,denominator))
