from itertools import product, cycle
from time import time


t1 = time()
with open(r"C:\Users\prane\Documents\Stuff\Python\Files_Input\p059_cipher.txt") as f:
    file = f.read()
file = file.split(",")
file = list(map(int, file))

checker = set([i for i in range(97, 123)] + [i for i in range(32, 91)])
key_list = list(product([i for i in range(97, 123)], repeat=3))
ans_key = []
high = 0
for key in key_list:
    k = 0
    for a, b in zip(file, cycle(key)):
        if a ^ b in checker:
            k += 1
    if k > high:
        high = k
        ans_key = key

# print(f'The encryption key is: {chr(ans_key[0])+chr(ans_key[1])+chr(ans_key[2])}')
string = ""
sum = 0
for a, b in zip(file, cycle(ans_key)):
    string += chr(a ^ b)
    sum += a ^ b
# print(string)
print(f"Answer is {sum}")
print(f"Process completed in {time()-t1}s")
