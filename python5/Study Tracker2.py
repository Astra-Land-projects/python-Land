from datetime import datetime
from pathlib import Path

topic = input("Topic: ").strip()
minutes = input("Minutes: ").strip()
line = f"{datetime.now().isoformat()} | {topic} | {minutes} min\n"

Path("study_log.txt").open("a", encoding="utf-8").write(line)
print("Saved.")