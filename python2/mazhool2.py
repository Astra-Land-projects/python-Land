from random import randint

def roll():
  dice_one = randint(1, 6)
  dice_two = randint(1, 6)

  return (dice_one, dice_two)

print(roll())