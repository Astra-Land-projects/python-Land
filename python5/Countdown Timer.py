import time

seconds = int(input("Seconds: "))

while seconds > 0:
    print(f"\rRemaining: {seconds}s", end="")
    time.sleep(1)
    seconds -= 1

print("\nTime's up!")