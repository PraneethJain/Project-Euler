from rich import print
from time import time


with open(r'C:\users\prane\Documents\Stuff\Python\Files_Input\p082_matrix.txt') as f:
    file=f.readlines()
file=[ele.strip() for ele in file]
for i,ele in enumerate(file):
    file[i]=list(map(str,ele.split(',')))

print(file)