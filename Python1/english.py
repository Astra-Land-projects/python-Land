import time
import random

def get_random_word():
    words = ["apple", "elephant", "tiger", "rabbit", "table","america","newyork","program"]
    return random.choice(words)

def main():
    print("word game")
   
    current_word = get_random_word()
    print(f"word start: {current_word}")
   
    start_time = time.time()
    time_limit = 20  # زمان محدود به ثانیه
   
    while True:
        last_char = current_word[-1]
        user_input = input(f"one word with letter '{last_char}' enter (remaining time: {time_limit} second): ")
       
        if time.time() - start_time > time_limit:
            print("time is up!")
            break
       
        if user_input and user_input[0].lower() == last_char.lower():
            current_word = user_input
            print(f"well! now my turn.")
           
            # کامپیوتر هم یک کلمه جدید تولید می‌کند.
            new_computer_word = get_random_word()
            print(f"computer: {new_computer_word}")
           
            current_word = new_computer_word
        else:
            print("word is not availible pls enter availble number.")

if __name__ == "__main__":
    main()