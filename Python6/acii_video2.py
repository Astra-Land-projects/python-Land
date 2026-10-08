import cv2
import os
import time

# کاراکترهایی که برای نمایش استفاده می‌شوند (از تاریک‌ترین به روشن‌ترین)
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def image_to_ascii(image, new_width=100):
    # تغییر اندازه تصویر برای جا شدن در ترمینال
    width, height = image.shape[1], image.shape[0]
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55) # 0.55 برای جبران فاصله خطوط ترمینال
    resized_image = cv2.resize(image, (new_width, new_height))
   
    # تبدیل به سیاه و سفید
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
   
    # تبدیل پیکسل‌ها به کاراکتر
    ascii_str = ""
    for pixel_value in gray_image.flatten():
        ascii_str += ASCII_CHARS[pixel_value // 25]
       
    return "\n".join([ascii_str[i:(i + new_width)] for i in range(0, len(ascii_str), new_width)])

# مسیر ویدیو خود را اینجا وارد کن
video_path = "arya.mp4"
cap = cv2.VideoCapture(video_path)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
           
        # تبدیل فریم به ASCII
        ascii_frame = image_to_ascii(frame)
       
        # پاک کردن صفحه ترمینال (در ویندوز 'cls' و در لینوکس/مک 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')
       
        print(ascii_frame)
       
        # کنترل سرعت پخش (می‌توانی تغییرش بدهی)
        time.sleep(0.03)
finally:
    cap.release()