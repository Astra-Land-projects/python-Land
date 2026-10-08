from pathlib import Path
import hashlib

seen = {}
for file in Path(".").rglob("*"):
    if file.is_file():
        h = hashlib.md5(file.read_bytes()).hexdigest()
        seen.setdefault(h, []).append(file)

for files in seen.values():
    if len(files) > 1:
        print("Duplicate group:")
        for f in files:
            print(" -", f)