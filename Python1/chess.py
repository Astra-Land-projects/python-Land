import chess
import random

def print_board(b):
    # نمایش شطرنج‌خانه‌ها به‌صورت متنی
    print(b.unicode(invert_color=True))
    print()

board = chess.Board()

while not board.is_game_over():
    # نمایش وضعیت فعلی
    print_board(board)

    # --- نوبت بازیکن ---
    move = input("حرکت خودتو وارد کن (مثلاً e2e4): ")
    try:
        board.push_san(move)          # تبدیل به SAN و اعمال روی صفحه
    except ValueError:
        print("حرکت نامعتبر، دوباره سعی کن.")
        continue                     # دوباره از بازیکن درخواست می‌کنیم

    # اگر بازی پس از حرکت بازیکن تمام شد، حلقه می‌شه تموم می‌شه
    if board.is_game_over():
        break

    # --- نوبت کامپیوتر (حرکت تصادفی) ---
    legal_moves = list(board.legal_moves)
    computer_move = random.choice(legal_moves)
    board.push(computer_move)
    print(f"کامپیوتر حرکت کرد: {board.san(computer_move)}\n")

# نمایش نتیجه نهایی
print_board(board)
result = board.result()
if result == "1-0":
    print("بازیکن پیروز شد! 🎉")
elif result == "0-1":
    print("کامپیوتر برنده شد! 🤖")
else:
    print("بازی مساوی شد. 🤝")
    #کتابخانه