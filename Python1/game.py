import random

def get_user_choice():
    user_input = input("choose one(rock,paper,scissors): ")
    while user_input not in ["rock", "paper", "scissors"]:
        print("pls choose one availble.")
        user_input = input("enter your choose(rock,paper,scissors): ")
    return user_input

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "you win!"
    else:
        return "computer win!"

def play_game():
    print("welcome to rock,paper,scissors!")
   
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
       
        print(f"you: {user_choice} | computer: {computer_choice}")
       
        result = determine_winner(user_choice, computer_choice)
        print(result)
       
        play_again = input("do you want play again: ").lower()
        if play_again != 'yes':
            break

play_game()