N = 8

board = [
    ["."] * N
    for _ in range(N)
]


def safe(row, col):

    for r in range(row):

        if board[r][col] == "Q":
            return False

        distance = row - r

        if (
            col - distance >= 0
            and board[r][col - distance] == "Q"
        ):
            return False

        if (
            col + distance < N
            and board[r][col + distance] == "Q"
        ):
            return False

    return True


def solve(row):

    if row == N:
        return True

    for col in range(N):

        if safe(row, col):

            board[row][col] = "Q"

            if solve(row + 1):
                return True

            board[row][col] = "."

    return False


solve()

for row in board:
    print(" ".join(row))