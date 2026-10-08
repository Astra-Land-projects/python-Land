import random

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 12)

def check_winner(board):
    # بررسی ردیف‌ها
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True
           
    # بررسی ستون‌ها
    for col in range(len(board)):
        if all([board[row][col] == board[0][col] and board[0][col] != ' ' for row in range(len(board))]):
            return True
           
    # بررسی قطرها
    if all([board[i][i] == board[0][0] and board[0][0] != ' ' for i in range(len(board))]) or \
       all([board[i][len(board)-1-i] == board[0][-1] and board[0][-1] != ' ' for i in range(len(board))]):
        return True
       
    return False

def tic_tac_toe():
    board = [[' '] * 4 for _ in range(4)]
   
    while True:
        print_board(board)
       
        player_move = int(input("choose one (1-16) (player 1 - X) player one: ")) - 1
        x, y = divmod(player_move, 4)
       
        if board[x][y] == ' ':
            board[x][y] = 'X'
           
            if check_winner(board):
                print_board(board)
                print("you win!")
                break
               
            player2_move = int(input("choose one (player 2 - O) player two: ")) - 1
            x, y = divmod(player2_move, 4)

            if board[x][y] == " ":
                board[x][y]='O'
               
                if check_winner(board):
                    print_board(board)
                    print("you win!")
                    break
                   
                computer_move = random.choice([(i,j) for i in range(4) for j in range(4) if board[i][j]==' '] )
                x, y = computer_move
                board[x][y]='Z'
               
                if check_winner(board):
                    print_board(board)
                    print("computer win!")
                    break
               
tic_tac_toe()