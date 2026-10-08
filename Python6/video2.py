import cv2
from ffpyplayer.player import MediaPlayer
import time

# مسیر ویدیوی خودت
video_path = "arya.mp4"

# باز کردن ویدیو با OpenCV
cap = cv2.VideoCapture(video_path)

# باز کردن پخش‌کننده صدا با ffpyplayer
player = MediaPlayer(video_path)

print("درحال پخش... برای بستن دکمه 'q' را بزن.")

while True:
    # خواندن فریم ویدیو
    ret, frame = cap.read()
   
    # گرفتن فریم صوتی و هماهنگی با ویدیو
    audio_frame, val = player.get_frame()

    # اگر ویدیو تموم شد یا مشکلی پیش اومد
    if not ret:
        break
   
    # نمایش تصویر
    if frame is not None:
        cv2.imshow('Video Player', frame)
   
    # هماهنگی صدا با ویدیو (اگر صدا تموم شد یا به آخر رسید)
    if val == 'eof':
        break
       
    # دکمه خروج
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# آزاد کردن منابع
cap.release()
cv2.destroyAllWindows()
player.close_player()