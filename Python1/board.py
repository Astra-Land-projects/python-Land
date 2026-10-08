class Backgammon:
    def __init__(self):
        self.board = [0] * 24  # 24 خانه
        self.players = ['A', 'B']
        self.current_player = 0

    def print_board(self):
        print("Board:")
        for i in range(24):
            print(f"{i + 1}: {self.board[i]}")

    def move(self, player, from_pos, to_pos):
        if self.board[from_pos - 1] > 0 and (to_pos - from_pos) <= 6:
            self.board[from_pos - 1] -= 1
            self.board[to_pos - 1] += 1

    def play_game(self):
        while True:
            self.print_board()
            current_player_name = self.players[self.current_player]
            from_position = int(input(f"Player {current_player_name}, enter your move from position (1-24): "))
            to_position = int(input(f"Player {current_player_name}, enter your move to position (1-24): "))
           
            if not (from_position in range(1,25) and to_position in range(1,25)):
                print("Invalid positions!")
                continue
           
            self.move(current_player_name, from_position, to_position)
           
            # Switch players
            self.current_player ^= 1

game = Backgammon()
game.play_game()