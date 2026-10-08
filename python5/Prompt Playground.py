import json
from datetime import datetime

history = []

while True:
    p = input("Prompt (/history /save /exit): ")
    if p == "/exit": break
    if p == "/history":
        print(history)
        continue
    if p == "/save":
        with open("prompts.json", "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
        print("Saved")
        continue
    history.append({"time": datetime.now().isoformat(), "prompt": p})
    print("Prompt stored.")