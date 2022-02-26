from time import time


def straight(L):
    return all(L[i + 1] - L[i] == 1 for i in range(0, 4))


def flush(L):
    return len(set(L)) == 1


def royal_flush(hand):
    num_list = [ele[0] for ele in hand]
    num_list = list(map(lambda x: x.replace("T", "10"), num_list))
    num_list = list(map(lambda x: x.replace("J", "11"), num_list))
    num_list = list(map(lambda x: x.replace("Q", "12"), num_list))
    num_list = list(map(lambda x: x.replace("K", "13"), num_list))
    num_list = list(map(lambda x: x.replace("A", "14"), num_list))
    num_list = list(map(int, num_list))
    suite_list = [ele[1] for ele in hand]
    num_list.sort()
    suite_list.sort()
    return (
        straight(num_list) and flush(suite_list) and all(ele >= 10 for ele in num_list)
    )


def straight_flush(hand):
    num_list = [ele[0] for ele in hand]
    num_list = list(map(lambda x: x.replace("T", "10"), num_list))
    num_list = list(map(lambda x: x.replace("J", "11"), num_list))
    num_list = list(map(lambda x: x.replace("Q", "12"), num_list))
    num_list = list(map(lambda x: x.replace("K", "13"), num_list))
    num_list = list(map(lambda x: x.replace("A", "14"), num_list))
    num_list = list(map(int, num_list))
    suite_list = [ele[1] for ele in hand]
    num_list.sort()
    suite_list.sort()
    return straight(num_list) and flush(suite_list)


def four_of_a_kind(L):
    return any(L.count(L[i]) == 4 for i in range(0, 5))


def three_of_a_kind(L):
    return any(L.count(L[i]) == 3 for i in range(0, 5))


def pair(L):
    return any(L.count(L[i]) == 2 for i in range(0, 5))


def two_pairs(L):
    temp = [i for i in L]
    i = 0
    for ele in temp:
        if temp.count(ele) == 2:
            temp.remove(ele)
            temp.remove(ele)
            i += 1
    if i == 2:
        return True
    return False


def full_house(L):
    return three_of_a_kind(L) and pair(L)


def pairing(L):
    for ele in L:
        if L.count(ele) == 2:
            return ele


def checkwin(h):
    handlist = h.split()
    hand1 = handlist[0:5]
    num_list_1 = [ele[0] for ele in hand1]
    num_list_1 = list(map(lambda x: x.replace("T", "10"), num_list_1))
    num_list_1 = list(map(lambda x: x.replace("J", "11"), num_list_1))
    num_list_1 = list(map(lambda x: x.replace("Q", "12"), num_list_1))
    num_list_1 = list(map(lambda x: x.replace("K", "13"), num_list_1))
    num_list_1 = list(map(lambda x: x.replace("A", "14"), num_list_1))
    num_list_1 = list(map(int, num_list_1))
    suite_list_1 = [ele[1] for ele in hand1]
    num_list_1.sort()
    suite_list_1.sort()
    hand2 = handlist[5:10]
    num_list_2 = [ele[0] for ele in hand2]
    num_list_2 = list(map(lambda x: x.replace("T", "10"), num_list_2))
    num_list_2 = list(map(lambda x: x.replace("J", "11"), num_list_2))
    num_list_2 = list(map(lambda x: x.replace("Q", "12"), num_list_2))
    num_list_2 = list(map(lambda x: x.replace("K", "13"), num_list_2))
    num_list_2 = list(map(lambda x: x.replace("A", "14"), num_list_2))
    num_list_2 = list(map(int, num_list_2))
    suite_list_2 = [ele[1] for ele in hand2]
    num_list_2.sort()
    suite_list_2.sort()
    if royal_flush(hand1) or royal_flush(hand2):
        return royal_flush(hand1)
    elif straight_flush(hand1) or straight_flush(hand2):
        return straight_flush(hand1)
    elif four_of_a_kind(num_list_1) or four_of_a_kind(num_list_2):
        return four_of_a_kind(num_list_1)
    elif full_house(num_list_1) or full_house(num_list_2):
        return full_house(num_list_1)
    elif flush(num_list_1) or flush(num_list_2):
        return flush(num_list_1)
    elif straight(num_list_1) or straight(num_list_2):
        return straight(num_list_1)
    elif three_of_a_kind(num_list_1) or three_of_a_kind(num_list_2):
        return three_of_a_kind(num_list_1)
    elif two_pairs(num_list_1) or two_pairs(num_list_2):
        return two_pairs(num_list_1)
    elif pair(num_list_1) or pair(num_list_2):
        if pair(num_list_1) and pair(num_list_2):
            if pairing(num_list_1) == pairing(num_list_2):
                repeated = pairing(num_list_1)
                num_list_1.remove(repeated)
                num_list_1.remove(repeated)
                num_list_2.remove(repeated)
                num_list_2.remove(repeated)
                return max(num_list_1) > max(num_list_2)
            else:
                return pairing(num_list_1) > pairing(num_list_2)
        else:
            return pair(num_list_1)
    else:
        return max(num_list_1) > max(num_list_2)


t1 = time()
with open(r"C:\Users\prane\Documents\Stuff\Python\Files_Input\p054_poker.txt") as f:
    file = f.read()
file = file.split("\n")
file.pop()
ans = 0
for h in file:
    if checkwin(h):
        ans += 1

print(f"Player 1 wins {ans} times")
print(f"Process completed in {time()-t1}s")
