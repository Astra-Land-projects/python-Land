import csv

path = input("CSV file: ").strip()
col = input("Column name: ").strip()
value = input("Match value: ").strip()

with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    if row.get(col, "") == value:
        print(row)