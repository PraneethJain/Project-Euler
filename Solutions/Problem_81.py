from time import time
from rich import print

t1=time()
with open(r'C:\users\prane\Documents\Stuff\Python\Files_Input\p081_matrix.txt') as f:
    file=f.readlines()
file=[ele.strip() for ele in file]
for i,ele in enumerate(file):
    file[i]=list(map(int,ele.split(',')))

for i in range(78,-1,-1): 
    file[79][i] += file[79][i+1]
    file[i][79] += file[i+1][79]

for i in range(78,-1,-1):
    for j in range(78,-1,-1):
        file[i][j]+=min(file[i+1][j],file[i][j+1])

print(file[0][0])
print(f'Process completed in {time()-t1}s')
