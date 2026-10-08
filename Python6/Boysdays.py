import random
import time
import os
import sys

# پاک کردن صفحه
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# رنگ‌های ترمینال
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

def show_banner():
    clear()
    banner = f"""
{C.BOLD}{C.YELLOW}
    ╔══════════════════════════════════════════════╗
    ║                                              ║
    ║     🎉🎊  روز پسر مبارک!  🎊🎉              ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
{C.END}
"""
    print(banner)

def show_confetti():
    symbols = ['🎉', '🎊', '⭐', '✨', '💫', '🎈', '🎁', '🏆']
    for _ in range(5):
        line = ' '.join(random.choice(symbols) for _ in range(20))
        print(f"{C.CYAN}{line}{C.END}")
        time.sleep(0.3)

def show_messages():
    messages = [
        (C.BLUE, "پسر بودن یعنی قدرت، شجاعت و امید!"),
        (C.GREEN, "تو می‌تونی هر چیزی که بخوای بشی!"),
        (C.MAGENTA, "امروز روز توئه، جشن بگیر!"),
        (C.YELLOW, "به خودت افتخار کن، چون فوق‌العاده‌ای!"),
        (C.RED, "رویاهات رو دنبال کن، هیچ‌چیز غیرممکن نیست!"),
        (C.CYAN, "تو قهرمان زندگی خودتی!"),
    ]
   
    print(f"\n{C.BOLD}{C.WHITE}✨ پیام‌های ویژه روز پسر: ✨{C.END}\n")
    for color, msg in messages:
        print(f"{color}💙 {msg}{C.END}")
        time.sleep(1)

def show_heart():
    heart = f"""
{C.RED}
    ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
    ❤️  بهترین پسر دنیا  ❤️
    ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
{C.END}
"""
    print(heart)

def main():
    try:
        show_banner()
        time.sleep(1)
        show_confetti()
        time.sleep(1)
        show_messages()
        time.sleep(1)
        show_heart()
       
        print(f"\n{C.BOLD}{C.GREEN}🎂 تولدت مبارک نباشه، ولی روزت مبارک باشه! 🎂{C.END}")
        print(f"{C.YELLOW}امیدوارم همیشه شاد و موفق باشی! 💪{C.END}\n")
       
    except KeyboardInterrupt:
        print(f"\n{C.YELLOW}خداحافظ! روز خوبی داشته باشی! 👋{C.END}")

if __name__ == "__main__":
    main()