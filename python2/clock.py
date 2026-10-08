import time

def digital_clock():
    while True:
        # Get the current time
        current_time = time.strftime("%H:%M:%S")

        # Print the current time
        print(current_time, end="\r")  # Use \r to overwrite the previous time

        # Wait for 1 second
        time.sleep(1)

if __name__ == "__main__":
    digital_clock()