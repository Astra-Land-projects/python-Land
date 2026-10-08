import random

SIZE = 3
EMPTY = 0

def create_board():
    return [[(i * SIZE + j + 1) % (SIZE * SIZE)
             for j in range(SIZE)] for i in range(SIZE)]

def find_empty(b):
    for i in range(SIZE):
        for j in range(SIZE):
            if b[i][j] == EMPTY:
                return i, j

def show(b):
    print("\n" * 30)                     # به‌جای clear
    print("puzzle slide 3x3")
    print("-" * 20)
    for r in b:
        print("".join("   " if x == EMPTY else f"{x:3d}" for x in r))
    print("-" * 20)
    print("move: w(up) a(left) s(down) d(right)   (for exist q)")

def move(b, cmd):
    i, j = find_empty(b)
    di, dj = 0, 0
    if cmd == "w":  di, dj = -1, 0
    if cmd == "s":  di, dj =  1, 0
    if cmd == "a":  di, dj =  0,-1
    if cmd == "d":  di, dj =  0, 1
    ni, nj = i + di, j + dj
    if 0 <= ni < SIZE and 0 <= nj < SIZE:
        b[i][j], b[ni][nj] = b[ni][nj], b[i][j]
        return True
    return False

def shuffle(b, steps=150):
    for _ in range(steps):
        move(b, random.choice(["w","a","s","d"]))

def solved(b):
    exp = 1
    for i in range(SIZE):
        for j in range(SIZE):
            if i == SIZE-1 and j == SIZE-1:
                return b[i][j] == EMPTY
            if b[i][j] != exp:
                return False
            exp += 1
    return True

def main():
    board = create_board()
    shuffle(board)
    while True:
        show(board)
        if solved(board):
            print("good job! the puzzle is solve🎉")
            break
        cmd = input(">>> ").strip().lower()
        if cmd == "q":
            print("game is finish! good luke")
            break
        if not move(board, cmd):
            print("move not avalible!")

if __name__ == "__main__":
    main()