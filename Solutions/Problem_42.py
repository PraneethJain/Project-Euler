from time import time


def word_value(word: str) -> int:
    value = 0
    for letter in word:
        value += ord(letter.upper()) - 64
    return value


t1 = time()
with open(
    r"C:\Users\prane\Documents\Stuff\Python\Files_input\p042_words.txt", "r"
) as f:
    file = f.read()
file = file.replace('"', "")
words = file.split(",")

ans = 0

triangle_numbers = [int(i * (i + 1) / 2) for i in range(1, 30)]

for word in words:
    if word_value(word) in triangle_numbers:
        ans += 1
print(ans)
print(f"Process completed in {time()-t1}s")
