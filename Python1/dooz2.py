import random

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True
           
    for col in range(len(board)):
        if all([board[row][col] == board[0][col] and board[0][col] != ' ' for row in range(len(board))]):
            return True
           
    if all([board[i][i] == board[0][0] and board[0][0] != ' ' for i in range(len(board))]) or \
       all([board[i][len(board)-1-i] == board[0][-1] and board[0][-1] != ' ' for i in range(len(board))]):
        return True
       
    return False

def tic_tac_toe():
    board = [[' '] * 3 for _ in range(3)]
   
    while True:
        player_move = int(input("Choose a position from 1 to 9: ")) - 1
        x, y = divmod(player_move, 3)
       
        if board[x][y] == ' ':
            board[x][y] = 'X'
           
            if check_winner(board):
                print_board(board)
                print("You win!")
                break
               
            computer_move = random.choice([(i,j) for i in range(3) for j in range(3) if board[i][j]==' '])
            x, y = computer_move
            board[x][y]='O'
           
            if check_winner(board):
                print_board(board)
                print("Computer wins!")
                break
               
            print_board(board)

tic_tac_toe()