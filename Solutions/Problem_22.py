import time
t1 = time.time()
file = open(r"C:\Users\prane\Desktop\Stuff\Python\output_input\p022_names.txt","r")
f = file.readlines()
file.close
f[0]=f[0].replace('"','')
names = sorted(f[0].split(","))
ans = 0
for i in range(0,len(names)):
    ans += (i+1)*sum(ord(j) - 64 for j in list(names[i]))
print(ans,time.time()-t1)