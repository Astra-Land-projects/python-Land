import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # چاپ زمان به صورت خطی
        time.sleep(1)  # توقف به مدت یک ثانیه
        seconds -= 1
   
    print("time is up!")

def main():
    print("welcome to timer!")
   
    try:
        total_seconds = int(input("pls enter second for timer: "))
       
        if total_seconds <= 0:
            print("pls enter posstive number:")
            return
       
        countdown_timer(total_seconds)

    except ValueError:
        print("pls enter availble number:.")

if __name__ == "__main__":
    main()