# project_183_log_analyzer.py

from collections import Counter

log_file = input("Log file: ").strip()

counter = Counter()

with open(log_file, "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            counter["ERROR"] += 1
        if "WARNING" in line:
            counter["WARNING"] += 1
        if "INFO" in line:
            counter["INFO"] += 1

print(counter)