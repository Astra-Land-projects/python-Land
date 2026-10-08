board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def find_empty():

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:
                return row, col

    return None


def valid(number, row, col):

    for c in range(9):

        if board[row][c] == number:
            return False

    for r in range(9):

        if board[r][col] == number:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for r in range(
        box_row,
        box_row + 3
    ):

        for c in range(
            box_col,
            box_col + 3
        ):

            if board[r][c] == number:
                return False

    return True


def solve():

    empty = find_empty()

    if empty is None:
        return True

    row, col = empty

    for number in range(1, 10):

        if valid(number, row, col):

            board[row][col] = number

            if solve():
                return True

            board[row][col] = 0

    return False


solve()


for row in board:
    print(row)