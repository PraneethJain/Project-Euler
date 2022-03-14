from time import time

t1 = time()
with open(r"files\p022_names.txt", "r") as file:
    f = file.read()

f = f.replace('"', "")
names = sorted(f.split(","))
ans = 0
for i in range(0, len(names)):
    ans += (i + 1) * sum(ord(j) - 64 for j in list(names[i]))
print(ans)
print(f"Process completed in {time()-t1}s")
