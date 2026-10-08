import requests
import random

# ۱. دریافت لیست پروکسی‌های رایگان و فعال از سراسر جهان
def get_free_proxies():
    url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
    try:
        response = requests.get(url, timeout=10)
        proxy_list = response.text.splitlines()
        print(f"[+] تعداد {len(proxy_list)} پروکسی فعال دانلود شد!")
        return proxy_list
    except Exception as e:
        print("[-] خطا در دریافت لیست پروکسی‌ها:", e)
        return []

# ۲. ارسال درخواست با آی‌پی و موقعیت کاملاً رندوم
def fetch_with_random_proxy(proxies):
    if not proxies:
        return

    # انتخاب یک پروکسی رندوم از لیست
    random_proxy = random.choice(proxies)
    proxy_dict = {
        "http": f"http://{random_proxy}",
        "https": f"http://{random_proxy}"
    }

    print(f"\n[🔄] در حال تست پروکسی رندوم: {random_proxy}")

    try:
        # تست اتصال و بررسی آی‌پی و کشور مقصد
        res = requests.get("http://ip-api.com/json/", proxies=proxy_dict, timeout=5)
        data = res.json()
       
        print("==========================================")
        print(f"✅ اتصال موفقیت‌آمیز بود!")
        print(f"📍 کشور: {data.get('country')}")
        print(f"🌐 آی‌پی جدید: {data.get('query')}")
        print(f"🏢 ارائه‌دهنده: {data.get('isp')}")
        print("==========================================")

    except Exception:
        print("❌ این پروکسی پاسخ نداد، مجدداً تلاش می‌شود...")

# اجرای برنامه
if __name__ == "__main__":
    proxies = get_free_proxies()
   
    # ۳ بار تست برای دیدن تغییر آی‌پی و کشور در هر بار اجرا
    for i in range(3):
        print(f"\n--- درخواست شماره {i+1} ---")
        fetch_with_random_proxy(proxies)