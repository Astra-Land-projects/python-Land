import csv
from collections import Counter

file = input("CSV file: ")

with open(file, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print("Rows:", len(rows))

if not rows:
    raise SystemExit("Empty CSV")

columns = rows[0].keys()

for column in columns:
    values = [r[column] for r in rows]

    missing = sum(v == "" for v in values)

    print(f"\nColumn: {column}")
    print("Missing:", missing)
    print("Unique:", len(set(values)))

    numeric = []
    for v in values:
        try:
            numeric.append(float(v))
        except ValueError:
            pass

    if numeric:
        print("Min:", min(numeric))
        print("Max:", max(numeric))
        print("Average:", sum(numeric) / len(numeric))