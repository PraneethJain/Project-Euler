from sympy.ntheory import factorint

i = 1
while True:
    if all(len(factorint(j))==4 for j in range(i,i+4)):
        print(i)
        break
    i += 1
