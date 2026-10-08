# project_196_dice_simulator.py

import random
from collections import Counter

rolls = int(input("How many rolls? "))
counter = Counter(random.randint(1, 6) for _ in range(rolls))

for face in range(1, 7):
    print(face, ":", counter[face])