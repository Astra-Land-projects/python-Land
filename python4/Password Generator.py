# project_177_password_generator.py

import random
import string

length = int(input("Length: "))

chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))

print("Password:", password)