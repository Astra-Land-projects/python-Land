import random
import os

SIZE = 3                     # ابعاد پازل (۳×۳)
EMPTY = 0                    # مقدار خانه خالی

def create_board():
    """یک تخته‌ی حل‌شده می‌سازه."""
    board = [[(i * SIZE + j + 1) % (SIZE * SIZE)
              for j in range(SIZE)] for i in range(SIZE)]
    return board

def find_empty(board):
    """مختصات خانه خالی را برمی‌گردونه."""
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == EMPTY:
                return i, j

def display(board):
    """تخته را به صورت متنی چاپ می‌کنه."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("puzzle slide 3x3")
    print("-" * 20)
    for row in board:
        line = ""
        for val in row:
            line += "   " if val == EMPTY else f"{val:3d}"
        print(line)
    print("-" * 20)
    print("for move use them w/s/a/d or ↑/←/↓/→")
    print("for exist press q")

def move(board, direction):
    """خانه خالی را بر اساس جهت داده شده جابجا می‌کنه."""
    i, j = find_empty(board)
    di, dj = 0, 0
    if direction in ("w", "↑"):
        di, dj = -1, 0
    elif direction in ("s", "↓"):
        di, dj = 1, 0
    elif direction in ("a", "←"):
        di, dj = 0, -1
    elif direction in ("d", "→"):
        di, dj = 0, 1
    else:
        return False

    ni, nj = i + di, j + dj
    if 0 <= ni < SIZE and 0 <= nj < SIZE:
        board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
        return True
    return False

def shuffle(board, steps=100):
    """تخته را به‌صورت تصادفی در چند قدم مخلوط می‌کنه."""
    moves = ["w", "a", "s", "d"]
    for _ in range(steps):
        move(board, random.choice(moves))

def is_solved(board):
    """بررسی می‌کنه که آیا پازل حل شده یا نه."""
    expected = 1
    for i in range(SIZE):
        for j in range(SIZE):
            if i == SIZE - 1 and j == SIZE - 1:
                return board[i][j] == EMPTY
            if board[i][j] != expected:
                return False
            expected += 1
    return True

def main():
    board = create_board()
    shuffle(board, steps=200)   # مخلوط کردن اولیه
    while True:
        display(board)
        if is_solved(board):
            print("good job! the puzzle is solve 🎉")
            break
        cmd = input("move: ").strip().lower()
        if cmd == "q":
            print("game is finish! good luke")
            break
        if not move(board, cmd):
            print("move not avalible! try again.")
           
if __name__ == "__main__":
    main()