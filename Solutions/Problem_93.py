from itertools import combinations, combinations_with_replacement, permutations, product
from rich import print
from rich.progress import track
from time import time


t1 = time()

digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
digits_combinations = list(combinations(digits, 4))

operators = {"+", "-", "*", "/"}
operator_combinations = list(combinations_with_replacement(operators, 3))

dic = {}
for digits in track(digits_combinations,"Processing"):
    digit_permutations = list(permutations(digits))

    L = set()
    for operators in operator_combinations:
        operator_permutations = list(permutations(operators))

        for d in digit_permutations:
            for o in operator_permutations:
                try:
                    target1 = eval(f"{d[0]}{o[0]}{d[1]}{o[1]}{d[2]}{o[2]}{d[3]}")
                except:
                    pass
                try:
                    target2 = eval(f"{d[0]}{o[0]}({d[1]}{o[1]}{d[2]}){o[2]}{d[3]}")
                except:
                    pass
                try:
                    target3 = eval(f"{d[0]}{o[0]}({d[1]}{o[1]}{d[2]}{o[2]}{d[3]})")
                except:
                    pass
                try:
                    target4 = eval(f"({d[0]}{o[0]}{d[1]}){o[1]}({d[2]}{o[2]}{d[3]})")
                except:
                    pass
                for target in (target1, target2, target3, target4):
                    if target == int(target) and target > 0:
                        L.add(target)
    i = 0
    L = list(L)
    while L[i] == (i + 1):
        i += 1
    dic[digits] = i

key_list = list(dic.keys())
value_list = list(dic.values())
digits = key_list[value_list.index(max(value_list))]
digits = sorted(digits)
ans = ""
for digit in digits:
    ans += str(digit)

print(ans)
print(f"Process completed in {time()-t1} seconds")
