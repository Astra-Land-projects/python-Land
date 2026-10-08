import random
import time
import os

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
    for _ in range(3):
        line = ' '.join(random.choice(symbols) for _ in range(20))
        print(f"{C.MAGENTA}{line}{C.END}")
        time.sleep(0.3)

def show_messages():
    messages = [
        f"{C.BOLD}{C.CYAN}پسر بودن یعنی قدرت، یعنی امید، یعنی آینده!{C.END}",
        f"{C.BOLD}{C.GREEN}تو می‌تونی هر چیزی که بخوای بشی، فقط باور کن!{C.END}",
        f"{C.BOLD}{C.YELLOW}امروز روز توئه، پس لبخند بزن و بدرخش!{C.END}",
        f"{C.BOLD}{C.MAGENTA}قوی باش، مهربون باش، و هیچوقت تسلیم نشو!{C.END}",
        f"{C.BOLD}{C.BLUE}دنیا به پسرهای بااراده مثل تو افتخار می‌کنه!{C.END}",
    ]
   
    for msg in messages:
        print("\n" + msg)
        time.sleep(1.5)

def show_final():
    print(f"""
{C.BOLD}{C.RED}
    ╔══════════════════════════════════════════════╗
    ║                                              ║
    ║   {C.YELLOW}🎂 تولدت مبارک پسر خوب! 🎂{C.RED}              ║
    ║   {C.GREEN}🌟 بهترین‌ها رو برات آرزو می‌کنم 🌟{C.RED}       ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
{C.END}
""")

def main():
    show_banner()
    time.sleep(1)
    show_confetti()
    show_messages()
    show_final()
    show_confetti()
    print(f"\n{C.BOLD}{C.WHITE}✨ روز پسر مبارک داداش! ✨{C.END}\n")

if __name__ == "__main__":
    main()