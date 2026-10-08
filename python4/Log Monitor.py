from collections import Counter

path = input("Log file: ").strip()
c = Counter()

with open(path, encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line: c["ERROR"] += 1
        if "WARNING" in line: c["WARNING"] += 1
        if "INFO" in line: c["INFO"] += 1

print(c)