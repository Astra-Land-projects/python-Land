number = 50
hint = """welcome to number guess you can guess number between 1 to 100.Enter a number:"""

while True:
  user_guess = int(input(hint))

  if user_guess == number:
    print("good job that true!")
    break
  
  if user_guess > number:
    hint = "Enter smaller number:"
  else:
    hint = "Enter bigger number:"  