import cv2

# لیست کاراکترها از تیره به روشن
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def image_to_ascii(image_path, new_width=100):
    # ۱. خواندن عکس
    image = cv2.imread(image_path)
    if image is None:
        print("خطا: عکس پیدا نشد! مسیر رو چک کن.")
        return

    # ۲. تبدیل به خاکستری و تغییر اندازه
    width, height = image.shape[1], image.shape[0]
    aspect_ratio = height / width
    # ضریب 0.55 برای اینه که کاراکترهای ترمینال معمولاً مستطیلی هستن و اینجوری تصویر کشیده نمیشه
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = cv2.resize(image, (new_width, new_height))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # ۳. تبدیل پیکسل‌ها به کاراکتر
    ascii_str = ""
    for pixel_value in gray_image.flatten():
        # تقسیم بر ۲۵ برای اینکه عدد ۲۵۵ (سفید) به ایندکس‌های لیست ما (۰ تا ۱۰) تبدیل بشه
        ascii_str += ASCII_CHARS[pixel_value // 25]

    # ۴. ساختن خروجی نهایی
    ascii_img = "\n".join([ascii_str[i:(i + new_width)] for i in range(0, len(ascii_str), new_width)])
    print(ascii_img)

# اینجا اسم عکس خودت رو بنویس (مثلا photo.jpg)
image_to_ascii("arya.jpg")