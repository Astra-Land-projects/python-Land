from pathlib import Path

path = input("Text file: ").strip()
lines = [x.strip() for x in Path(path).read_text(encoding="utf-8").splitlines()]
clean = [x for x in lines if x]
clean = list(dict.fromkeys(clean))
out = path.rsplit(".", 1)[0] + "_clean.txt"
Path(out).write_text("\n".join(clean), encoding="utf-8")
print("Saved:", out)