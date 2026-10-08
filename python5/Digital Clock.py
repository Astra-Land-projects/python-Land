import time
from datetime import datetime

while True:
    now = datetime.now().strftime("%H:%M:%S")
    print(f"\r{now}", end="")
    time.sleep(1)