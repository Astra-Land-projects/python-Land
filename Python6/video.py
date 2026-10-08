import cv2

# ۱. مسیر فایل ویدیوی خودت رو اینجا بنویس
video_path = "arya.mp4"

# ۲. باز کردن ویدیو
cap = cv2.VideoCapture(video_path)

# چک می‌کنیم که آیا ویدیو اصلاً باز شده یا نه
if not cap.isOpened():
    print("خطا: نمی‌توانم ویدیو را باز کنم. مسیر فایل را چک کنید.")
    exit()

print("در حال پخش ویدیو... برای بستن، کلید 'q' را روی صفحه ویدیو فشار دهید.")

while cap.isOpened():
    # خواندن فریم به فریم ویدیو
    ret, frame = cap.read()

    if not ret:
        print("ویدیو به پایان رسید یا مشکلی در خواندن فریم‌ها وجود دارد.")
        break

    # ۳. نمایش ویدیو در یک پنجره
    cv2.imshow('My Video Player', frame)

    # ۴. کنترل سرعت پخش و خروج
    # عدد 25 یعنی ۲۵ میلی‌ثانیه صبر کن (بستگی به FPS ویدیو دارد)
    # اگر ویدیو خیلی سریع یا کند بود، این عدد رو تغییر بده
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# ۵. بستن همه چیز پس از اتمام
cap.release()
cv2.destroyAllWindows()