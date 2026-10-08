from pathlib import Path
from shutil import move

folder = Path(".")
for file in folder.iterdir():
    if file.is_file():
        ext = file.suffix[1:].lower() or "no_extension"
        target = folder / ext
        target.mkdir(exist_ok=True)
        move(str(file), str(target / file.name))
print("Done.")