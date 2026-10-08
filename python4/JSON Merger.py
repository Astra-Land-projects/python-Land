import json

a = json.load(open(input("First JSON: ").strip(), encoding="utf-8"))
b = json.load(open(input("Second JSON: ").strip(), encoding="utf-8"))

if isinstance(a, dict) and isinstance(b, dict):
    a.update(b)
    print(json.dumps(a, ensure_ascii=False, indent=2))
else:
    print(a + b)