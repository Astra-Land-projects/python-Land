import random

characters="0123456789!@#$_"
pass_list = []

password_length = 0

while password_length < 8:
  password_length = int(input("(حداقل 8 کاراکتر) طول رمز عبور خود رو وارد کنید"))


for i in range(password_length):
  char = random.choice(characters)
  pass_list.append(char)

random.shuffle(pass_list)

password = ""
for char in pass_list:
  password += char

print(password)