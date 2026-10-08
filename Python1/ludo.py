import random

class LudoGame:
    def __init__(self):
        # رنگ‌های ممکن
        self.all_colors = ['Red', 'Green', 'Blue', 'Yellow']
        self.players = []          # لیست دیکشنری‌های بازیکن
        self.computer_cnt = 0
        self.board_size = 52       # تعداد خانه‌های مسیر

    # -------------------------------------------------
    # انتخاب تعداد بازیکن و اینکه چندتا کامپیوتر باشند
    # -------------------------------------------------
    def setup_players(self):
        while True:
            try:
                total = int(input("player (2-4): "))
                if 2 <= total <= 4:
                    break
                print("number must be between 2-4.")
            except ValueError:
                print("pls enter number.")
        while True:
            try:
                self.computer_cnt = int(input(f"how many of {total} until the.) be computer players?{total}): "))
                if 0 <= self.computer_cnt <= total:
                    break
                print("number not availble.")
            except ValueError:
                print("pls enter number.")
        human_cnt = total - self.computer_cnt

        # ثبت بازیکن‌های انسانی
        for i in range(1, human_cnt + 1):
            self.players.append({
                'id'      : f'Human{i}',
                'type'    : 'human',
                'color'   : None,
                'position': 0,   # موقعیت شروع
                'finished': False
            })
        # ثبت بازیکن‌های کامپیوتری
        for i in range(1, self.computer_cnt + 1):
            self.players.append({
                'id'      : f'CPU{i}',
                'type'    : 'computer',
                'color'   : None,
                'position': 0,
                'finished': False
            })

    # -------------------------------------------------
    # انتخاب رنگ برای هر بازیکن (رنگ‌های تکراری مجاز نیستند)
    # -------------------------------------------------
    def choose_colors(self):
        available = self.all_colors.copy()
        for p in self.players:
            if p['type'] == 'human':
                while True:
                    choice = input(f"{p['id']}، choose the color ({', '.join(available)}): ")
                    if choice in available:
                        p['color'] = choice
                        available.remove(choice)
                        break
                    print("color is not avaible or someone already choose.")
            else:   # کامپیوتر
                p['color'] = random.choice(available)
                print(f"{p['id']} color {p['color']} take.")
                available.remove(p['color'])

    # -------------------------------------------------
    # پرتاب تاس (۱ تا ۶)
    # -------------------------------------------------
    def roll_dice(self):
        return random.randint(1, 6)

    # -------------------------------------------------
    # اجرای یک نوبت برای بازیکن مشخص
    # -------------------------------------------------
    def play_turn(self, player):
        print(f"\nturn {player['id']} ({player['color']})")
        if player['type'] == 'human':
            input("for throw dice press enter...")
        else:
            print("computer currentlly...")
        dice = self.roll_dice()
        print(f"number dice: {dice}")

        # حرکت مهره
        if not player['finished']:
            player['position'] = min(self.board_size, player['position'] + dice)
            print(f"{player['id']} to home {player['position']} arrive.")

            # بررسی اتمام بازی برای این بازیکن
            if player['position'] == self.board_size:
                player['finished'] = True
                print(f"{player['id']} win! 🎉")

    # -------------------------------------------------
    # حلقه اصلی بازی
    # -------------------------------------------------
    def start(self):
        self.setup_players()
        self.choose_colors()
        turn_index = 0
        while True:
            current = self.players[turn_index]
            self.play_turn(current)

            # بررسی پایان کامل بازی
            finished_players = [p for p in self.players if p['finished']]
            if len(finished_players) == len(self.players):
                print("\ngame is finish! reasult:")
                for i, p in enumerate(finished_players):
                    print(f"{i+1}. {p['id']} ({p['color']})")
                break

            turn_index = (turn_index + 1) % len(self.players)

# -------------------------
# اجرای بازی
# -------------------------
if __name__ == "__main__":
    game = LudoGame()
    game.start()