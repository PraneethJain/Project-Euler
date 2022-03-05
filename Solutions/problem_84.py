from rich import print
from rich.progress import track
from time import time
from random import randrange

t1 = time()
squares = [
    "GO",
    "A1",
    "CC1",
    "A2",
    "T1",
    "R1",
    "B1",
    "CH1",
    "B2",
    "B3",
    "J",
    "C1",
    "U1",
    "C2",
    "C3",
    "R2",
    "D1",
    "CC2",
    "D2",
    "D3",
    "FP",
    "E1",
    "CH2",
    "E2",
    "E3",
    "R3",
    "F1",
    "F2",
    "U2",
    "F3",
    "G2J",
    "G1",
    "G2",
    "CC3",
    "G3",
    "R4",
    "CH3",
    "H1",
    "T2",
    "H2",
]
squares_simple = [ele[:-1] for ele in squares]
num = [0] * 40
index = 0
ccpos = 1
chpos = 1
double_checker = [0, 0, 0]


def get_die(sides=4):
    return randrange(1, sides + 1)


def play_game():
    global index, double_checker, ccpos, chpos
    roll1 = get_die()
    roll2 = get_die()
    if roll1 == roll2:
        double_checker = [1] + double_checker[:2]
    else:
        double_checker = [0] + double_checker[:2]
    score = roll1 + roll2
    index = (index + score) % 40

    if ccpos > 16:
        ccpos = 1
    if chpos > 16:
        chpos = 1

    match squares_simple[index]:
        case "CC":
            match ccpos:
                case 1:
                    index = 0  # Go
                    ccpos += 1
                case 2:
                    index = 10  # Jail
                    ccpos += 1
                case _:
                    ccpos += 1
        case "CH":
            match chpos:
                case 1:
                    index = 0  # Go
                    chpos += 1
                case 2:
                    index = 10  # Jail
                    chpos += 1
                case 3:
                    index = squares.index("C1")
                    chpos += 1
                case 4:
                    index = squares.index("E3")
                    chpos += 1
                case 5:
                    index = squares.index("H2")
                    chpos += 1
                case 6:
                    index = squares.index("R1")
                    chpos += 1
                case 7:
                    try:
                        squares_simple.index("R", index)
                    except:
                        squares_simple.index("R")
                    chpos += 1
                case 8:
                    try:
                        squares_simple.index("R", index)
                    except:
                        squares_simple.index("R")
                    chpos += 1
                case 9:
                    try:
                        squares_simple.index("U", index)
                    except:
                        squares_simple.index("U")
                    chpos += 1
                case 10:
                    index = (index - 3) % 40
                    chpos += 1
                case _:
                    chpos += 1
        case "G2":
            index = 10  # Jail
        case _:
            pass

    if double_checker == [1, 1, 1]:
        index = 10  # Jail
    num[index] += 1


for i in track(range(1_000_000), "Processing"):
    play_game()

sorted_squares = [x for _, x in sorted(zip(num, squares), reverse=True)]
print(
    str(squares.index(sorted_squares[0]))
    + str(squares.index(sorted_squares[1]))
    + str(squares.index(sorted_squares[2]))
)
print(f"Process completed in {time()-t1} seconds.")
