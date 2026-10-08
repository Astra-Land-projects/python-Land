def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # بررسی سطرها و ستون‌ها
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # بررسی قطرها
    if (board[0][0] == board[1][1] == board[2][2] != " ") or (board[0][2] == board[1][1] == board[2][0] != " "):
        return True

    return False

def tic_tac_toe():
    # ایجاد تخته بازی
    board = [[" "] * 3 for _ in range(3)]
   
    current_player = 'X'
   
    for turn in range(9):  # حداکثر 9 نوبت وجود دارد
        print_board(board)
       
        row = int(input(f"player {current_player}، number row(2-0) enter: "))
        col = int(input(f"player {current_player}، number coluwn(2-0) enter: "))
       
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("move is not availble pls try again.")
            continue
       
        # قرار دادن علامت بازیکن فعلی روی تخته
        board[row][col] = current_player
       
        if check_winner(board):
            print_board(board)
            print(f"good job! player {current_player} win!")
            break
           
        current_player = 'O' if current_player == 'X' else 'X'
   
    else:
      print_board(board)
      print("game is tie!")

if __name__ == "__main__":
   tic_tac_toe()