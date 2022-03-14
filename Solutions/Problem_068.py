from time import time


t1 = time()
num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
L = []
ans_list = []
num_list = []

for sum in range(11, 30):
    for a in num_set:
        for b in num_set.difference({a}):
            c = sum - a - b
            if c in num_set.difference({a, b}):
                for d in num_set.difference({a, b, c}):
                    e = sum - c - d
                    if e in num_set.difference({a, b, c, d}):
                        for f in num_set.difference({a, b, c, d, e}):
                            g = sum - f - e
                            if g in num_set.difference({a, b, c, d, e, f}):
                                for h in num_set.difference({a, b, c, d, e, f, g}):
                                    i = sum - f - h
                                    if i in num_set.difference(
                                        {a, b, c, d, e, f, g, h}
                                    ):
                                        j = sum - h - b
                                        if j in num_set.difference(
                                            {a, b, c, d, e, f, g, h, i}
                                        ):
                                            L.append(
                                                [
                                                    [a, b, c],
                                                    [d, c, e],
                                                    [g, e, f],
                                                    [i, f, h],
                                                    [j, h, b],
                                                ]
                                            )
for sol_list in L:
    n = sol_list.index(min(sol_list))
    if n == 0:
        ans_list.append(sol_list)
    else:
        ans_list.append(sol_list[n:] + sol_list[:n])
for sol_list in ans_list:
    num = ""
    for sol in sol_list:
        for x in sol:
            num += str(x)
    num_list.append(int(num))

num_list = [i for i in num_list if len(str(i)) == 16]
print(max(num_list))
print(f"Process completed in {time()-t1}s")
