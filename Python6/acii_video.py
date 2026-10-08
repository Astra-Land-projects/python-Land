import cv2
import os
import time
from ffpyplayer.player import MediaPlayer # این خط رو اضافه کن

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def image_to_ascii(image, new_width=100):
    width, height = image.shape[1], image.shape[0]
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = cv2.resize(image, (new_width, new_height))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    ascii_str = ""
    for pixel_value in gray_image.flatten():
        ascii_str += ASCII_CHARS[pixel_value // 25]
    return "\n".join([ascii_str[i:(i + new_width)] for i in range(0, len(ascii_str), new_width)])

video_path = "arya.mp4" # مسیر فایل ویدیوت
cap = cv2.VideoCapture(video_path)
player = MediaPlayer(video_path) # این بخش صدا رو پخش می‌کنه

try:
    while cap.isOpened():
        ret, frame = cap.read()
        audio_frame, val = player.get_frame() # دریافت صدا
       
        if not ret:
            break
       
        # اگر صدا به پایان رسید یا زمانش تموم شد، حلقه رو کنترل کن
        if val == 'eof':
            break
           
        ascii_frame = image_to_ascii(frame)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ascii_frame)
       
        # دیگه به time.sleep نیاز نداریم چون صدا خودش سرعت ویدیو رو تنظیم می‌کنه
finally:
    cap.release()
    player.close_player() # بستن پلیر صدا