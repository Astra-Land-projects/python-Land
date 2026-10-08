from google import genai

# ۱. مقداردهی اولیه کلاینت جمنای
client = genai.Client(api_key="AQ.Ab8RN6LH3Sy_esFLj-sbd4wGicTb5uyXufvxZjsTOJW-NcLONw")

# ۲. شروع یک جلسه چت با مدیریت خودکار تاریخچه
chat = client.chats.create(model="gemini-2.5-flash")

print("--- چت‌بات جمنای آماده است! (برای خروج exit را بنویسید) ---\n")

while True:
    user_input = input("شما: ")
   
    if user_input.lower() in ['exit', 'خروج']:
        print("خدانگهدار!")
        break

    # ارسال پیام به Gemini و دریافت پاسخ
    response = chat.send_message(user_input)
    print(f"\nجمنای: {response.text}\n")