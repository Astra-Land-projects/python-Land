import re

pw = input("Password: ")
score = 0

if len(pw) >= 8: score += 1
if re.search(r"[a-z]", pw): score += 1
if re.search(r"[A-Z]", pw): score += 1
if re.search(r"\d", pw): score += 1
if re.search(r"[^\w\s]", pw): score += 1

levels = {0:"Very weak", 1:"Weak", 2:"Okay", 3:"Good", 4:"Strong", 5:"Very strong"}
print(levels[score])