import random

def scramble_text(text):
    """متن رو به صورت تصادفی جابجا می‌کنه."""
    chars = list(text)
    random.shuffle(chars)
    return ''.join(chars)

def play_puzzle(original_text):
    """پازل رو اجرا می‌کنه."""
    scrambled_text = scramble_text(original_text)
    print("puzzle: ", scrambled_text)
   
    attempts = 3  # تعداد تلاش‌های مجاز
    while attempts > 0:
        guess = input("guess main text: ")
        if guess == original_text:
            print("good job! that is ture! 🎉")
            return
        else:
            attempts -= 1
            print(f"sorry! that is mistake. {attempts} remain try.")

    print("sorry! you can not guess answer: ", original_text)

# متن اصلی که می‌خوای پازلش رو درست کنی
original_message = "I love you so much"

play_puzzle(original_message)