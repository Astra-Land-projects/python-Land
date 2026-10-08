from datetime import datetime
import time

target = input("Alarm time HH:MM:SS: ").strip()

print("Waiting...")
while True:
    now = datetime.now().strftime("%H:%M:%S")
    if now == target:
        print("ALARM!")
        break
    time.sleep(0.5)