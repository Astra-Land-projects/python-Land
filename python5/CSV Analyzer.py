import csv

path = input("CSV file: ").strip()
col = input("Numeric column: ").strip()

values = []
with open(path, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try: values.append(float(row[col]))
        except: pass

print("Count:", len(values))
print("Min:", min(values))
print("Max:", max(values))
print("Avg:", sum(values) / len(values))