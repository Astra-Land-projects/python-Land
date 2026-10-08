# project_187_json_formatter.py

import json

raw = input("Paste JSON: ")

data = json.loads(raw)
print(json.dumps(data, indent=2, ensure_ascii=False))