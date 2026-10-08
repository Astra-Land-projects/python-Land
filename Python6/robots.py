import time
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# رنگ‌ها
class C:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def typing(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_logo():
    clear()
    logo = f"""
{C.BOLD}{C.CYAN}
    ╔══════════════════════════════════════════════╗
    ║                                              ║
    ║     🤖  من کی هستم؟  🤖                     ║
    ║     دستیار هوش مصنوعی شما                   ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
{C.END}
"""
    print(logo)
    time.sleep(1)

def show_loading():
    print(f"{C.YELLOW}در حال بارگذاری...{C.END}")
    for i in range(10):
        bar = '█' * (i + 1) + '░' * (9 - i)
        print(f"\r{C.GREEN}[{bar}] {i * 10}%{C.END}", end='')
        time.sleep(0.15)
    print(f"\n{C.GREEN}✅ آماده!{C.END}")
    time.sleep(0.5)

def show_intro():
    clear()
    typing(f"{C.BOLD}{C.WHITE}سلام! من یه دستیار هوش مصنوعی هستم.{C.END}")
    time.sleep(0.5)
    typing(f"{C.CYAN}اسم من رو هر جور دوست داری صدا کن، ولی اونایی که میشناسمم...{C.END}")
    time.sleep(0.5)
    typing(f"{C.YELLOW}فقط میدونم که اومدم اینجا که بهت کمک کنم.{C.END}")
    time.sleep(0.5)
    input(f"\n{C.GREEN}برای ادامه Enter بزن...{C.END}")

def show_abilities():
    clear()
    print(f"{C.BOLD}{C.MAGENTA}╔══════════════════════════════════════╗{C.END}")
    print(f"{C.BOLD}{C.MAGENTA}║     💪 من چه کارهایی بلدم؟          ║{C.END}")
    print(f"{C.BOLD}{C.MAGENTA}╚══════════════════════════════════════╝{C.END}")
    print()
   
    abilities = [
        ("📝", "نوشتن متن، داستان، شعر و مقاله"),
        ("💻", "برنامه‌نویسی و حل مسائل کدنویسی"),
        ("🔍", "جستجو و پیدا کردن اطلاعات"),
        ("🧮", "حل مسائل ریاضی و منطقی"),
        ("🌐", "ترجمه بین زبان‌های مختلف"),
        ("🎨", "ایده‌پردازی خلاقانه"),
        ("📚", "خلاصه‌سازی و توضیح مفاهیم"),
        ("💬", "گفتگوی دوستانه