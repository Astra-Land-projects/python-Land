# project_195_guess_the_word.py

import random

words = ["python", "flutter", "telegram", "machine", "learning"]
secret = random.choice(words)
guessed = ["_"] * len(secret)
tries = 6

while tries > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    guess = input("Letter: ").lower().strip()

    if guess in secret:
        for i, ch in enumerate(secret):
            if ch == guess:
                guessed[i] = guess
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)

if "_" not in guessed:
    print("You win:", secret)
else:
    print("Game over. Word was:", secret)