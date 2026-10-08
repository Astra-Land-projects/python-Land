board = [" "] * 9


def show():

    print()
    print(
        f"{board[0]} | {board[1]} | {board[2]}"
    )
    print("--+---+--")
    print(
        f"{board[3]} | {board[4]} | {board[5]}"
    )
    print("--+---+--")
    print(
        f"{board[6]} | {board[7]} | {board[8]}"
    )
    print()


def winner(player):

    combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in combinations
    )


def minimax(is_ai):

    if winner("O"):
        return 1

    if winner("X"):
        return -1

    if " " not in board:
        return 0

    if is_ai:

        best = -999

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best = max(best, score)

        return best

    else:

        best = 999

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best = min(best, score)

        return best


def ai_move():

    best_score = -999
    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:

                best_score = score
                move = i

    board[move] = "O"


while True:

    show()

    move = int(
        input(
            "Choose position 1-9: "
        )
    ) - 1

    if (
        move < 0
        or move > 8
        or board[move] != " "
    ):
        print("Invalid move.")
        continue

    board[move] = "X"

    if winner("X"):
        show()
        print("You win!")
        break

    if " " not in board:
        show()
        print("Draw!")
        break

    ai_move()

    if winner("O"):
        show()
        print("AI wins!")
        break