import random

class Backgammon:
    def __init__(self):
        self.board = [2] * 24     # هر خانه ۲ مهره داره
        self.players = ['X', 'O']
        self.current_player = 0
        self.dice = [0, 0]        # تاس‌ها

    def print_board(self):
        print("Board:")
        for i in range(24):
            print(f"{i + 1}: {self.board[i]}")

    def roll_dice(self):
        self.dice = [random.randint(1, 6), random.randint(1, 6)]
        print(f"Dice: {self.dice[0]}, {self.dice[1]}")

    def move(self, player, from_pos, to_pos):
        if 1 <= from_pos <= 24 and 1 <= to_pos <= 24:
            if self.board[from_pos - 1] > 0:
                if abs(from_pos - to_pos) <= max(self.dice):
                    self.board[from_pos - 1] -= 1
                    self.board[to_pos - 1] += 1
                    print(f"Move from {from_pos} to {to_pos} successful.")
                else:
                    print("Invalid move (out of dice range).")
            else:
                print("No piece at that position.")
        else:
            print("Invalid position.")

    def play_game(self):
        while True:
            self.print_board()
            self.roll_dice()
            current_player_name = self.players[self.current_player]
            print(f"\nPlayer {current_player_name}'s turn:")
            for _ in range(2):  # دو حرکت بر اساس تاس
                from_position = int(input(f"Player {current_player_name}, enter your move from position (1-24): "))
                to_position = int(input(f"Player {current_player_name}, enter your move to position (1-24): "))
                self.move(current_player_name, from_position, to_position)
            self.current_player = (self.current_player + 1) % 2

# -------------------------
# اجرای بازی
# -------------------------
if __name__ == "__main__":
    game = Backgammon()
    game.play_game()