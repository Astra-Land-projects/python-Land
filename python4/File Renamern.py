# project_181_file_renamer.py

from pathlib import Path

folder = Path(".")
prefix = input("Prefix: ").strip()

files = [f for f in folder.iterdir() if f.is_file()]

for i, file in enumerate(files, start=1):
    new_name = f"{prefix}_{i}{file.suffix}"
    file.rename(folder / new_name)
    print(file.name, "->", new_name)