import requests

proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080'
}

try:
    # ارسال درخواست از طریق پروکسی شخصی پایتون
    response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
    print("پاسخ موفقیت‌آمیز از طریق پروکسی:")
    print(response.json())
except Exception as e:
    print("خطا در اتصال:", e)