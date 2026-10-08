import chess

def print_board(b):
    # نمایش شطرنج‌خانه‌ها به‌صورت متنی
    print(b.unicode(invert_color=True))
    print()

board = chess.Board()

while not board.is_game_over():
    # نمایش وضعیت فعلی
    print_board(board)

    # --- نوبت بازیکن اول ---
    if board.turn == chess.WHITE:
        player = 1
    else:
        player = 2

    move = input(f"نوبت بازیکن {player}: حرکت خودتو وارد کن (مثلاً e2e4): ")
    try:
        board.push_san(move)          # تبدیل به SAN و اعمال روی صفحه
    except ValueError:
        print("حرکت نامعتبر، دوباره سعی کن.")
        continue                     # دوباره از بازیکن درخواست می‌کنیم

    # اگر بازی پس از حرکت بازیکن تمام شد، حلقه می‌شه تموم می‌شه
    if board.is_game_over():
        break

# نمایش نتیجه نهایی
print_board(board)
result = board.result()
if result == "1-0":
    print("بازیکن اول پیروز شد! 🎉")
elif result == "0-1":
    print("بازیکن دوم برنده شد! 🤖")
else:
    print("بازی مساوی شد. 🤝")