import random
import chess


board = chess.Board()


def show():

    print(board)


while not board.is_game_over():

    show()

    print("\nYour turn.")

    legal_moves = list(
        board.legal_moves
    )

    print("\nLegal moves:")

    for move in legal_moves:
        print(move, end=" ")

    print()

    user_move = input(
        "\nMove (e2e4): "
    )

    try:

        move = chess.Move.from_uci(
            user_move
        )

        if move not in board.legal_moves:
            print("Illegal move.")
            continue

        board.push(move)

    except ValueError:

        print("Invalid move.")
        continue

    if board.is_game_over():
        break

    ai_move = random.choice(
        list(board.legal_moves)
    )

    print(
        "\nAI move:",
        ai_move
    )

    board.push(ai_move)


show()

print(
    "\nGame over:",
    board.result()
)