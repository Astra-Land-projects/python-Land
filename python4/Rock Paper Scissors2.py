import random

choices = ["rock", "paper", "scissors"]
while True:
    user = input("rock/paper/scissors or exit: ").lower()
    if user == "exit":
        break
    ai = random.choice(choices)
    print("AI:", ai)
    if user == ai:
        print("Draw")
    elif (user, ai) in [("rock","scissors"), ("paper","rock"), ("scissors","paper")]:
        print("You win")
    else:
        print("AI wins")