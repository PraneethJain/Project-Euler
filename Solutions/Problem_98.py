from rich import print
from time import time
from fraction import square_check

t1 = time()


def do_map(dic: dict, word: str):
    for ele in dic:
        word = word.replace(ele, dic[ele])
    return word


squares = [1]
i = 2
while squares[-1] < 10**8:
    squares.append(i**2)
    i += 1


def square_anagram(word1: str, word2: str) -> int:
    for square in squares:
        if "0" in str(square):
            continue
        if len(str(square)) == len(word1) and len(set(str(square))) == len(set(word1)):
            dic = dict(zip(list(word1), list(str(square))))
            num2 = int(do_map(dic, word2))
            if num2 in squares:
                return max(square, num2)
    return 0


with open(r"files/p098_words.txt") as f:
    words = f.read().split(",")
words = [ele.replace('"', "") for ele in words]
words_lettered = [set(ele) for ele in words]
anagrams = set()

for i, letter_set in enumerate(words_lettered):
    if words_lettered.count(letter_set) > 1:
        try:
            word1 = words[i]
            word2 = words[words_lettered.index(letter_set, i + 1)]
            if sorted(word1) == sorted(word2):
                anagrams.add((word1, word2))
        except:
            pass


high = 0
worda, wordb = "", ""
for word1, word2 in anagrams:
    current = square_anagram(word1, word2)
    if current > high:
        high = current
        worda = word1
        wordb = word2

print(f" {worda} , {wordb} : {high}")
print(f"Process completed in {time()-t1} seconds")
