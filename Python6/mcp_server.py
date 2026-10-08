import requests
import json
from google import genai

# =============================================================
# ۱. تنظیم کلیدهای API (کلیدهای خودت را اینجا وارد کن)
# =============================================================
GEMINI_API_KEY = "AQ.Ab8RN6KswI9XYgbCIwfiPeQ_3QQbI3d2JHN0b7Y7s6EbhXMTYg"
GROQ_API_KEY = "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"
OPENROUTER_API_KEY = "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"
GAPGPT_API_KEY = "sk-v9acBR7jCi4wGoA6x6RbNvW8XAYntvCJDil3mHYNjgmC3szw"
ZAI_API_KEY = "f3e7b97af78d4d6989722748bae3adab.3AusMBrUnVBCVgId"
DEEPSEEK_API_KEY = "sk-078e29c1320b4d23be2e8cb72d167f2b"

# آدرس Ollama روی سیستم خودت (بدون نیاز به کلید)
OLLAMA_URL = "http://localhost:11434/api/generate"

# راه اندازی کلاینت Gemini
gemini_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY != "AQ.Ab8RN6KswI9XYgbCIwfiPeQ_3QQbI3d2JHN0b7Y7s6EbhXMTYg" else None

# =============================================================
# ۲. تعریف چارت سازمانی و نقش ایجنت‌ها
# =============================================================
BOTS = {
    "Gemini": {
        "role": "پژوهشگر زنده و پردازش فایل/دیتا",
        "system_prompt": "تو جمنای هستی. وظیفه‌ات تحلیل داده‌ها و ارائه اطلاعات به‌روز و دقیق است."
    },
    "Groq": {
        "role": "پردازشگر فوق‌سریع و تحلیل‌گر منطقی (Llama 3)",
        "system_prompt": "تو ایجنت قدرتمند روی بستر Groq هستی. وظیفه‌ات تحلیل سریع، بازبینی خطاهای منطقی و پاسخگویی آنی است."
    },
    "DeepSeek": {
        "role": "برنامه‌نویس ارشد و توسعه‌دهنده کد",
        "system_prompt": "تو دیپ‌سیک هستی. وظیفه‌ات نوشتن کدهای تمیز، بهینه و رفع خطاهای برنامه‌نویسی است."
    },
    "OpenRouter": {
        "role": "مشاور مدل‌های عمومی و ایده‌پرداز تکنیکال",
        "system_prompt": "تو ایجنت متصل به OpenRouter هستی. وظیفه‌ات ارائه ایده‌های مکمل و راه‌حل‌های جایگزین است."
    },
    "GapGPT": {
        "role": "بومی‌ساز و پشتیبان زبان فارسی",
        "system_prompt": "تو گپ‌جی‌پوتی هستی. وظیفه‌ات بررسی متون، بومی‌سازی و روان‌سازی ارتباط فارسی با کاربر است."
    },
    "Z.ai": {
        "role": "تحلیل‌گر تخصصی و ارزیابی کیفیت خروجی (QA)",
        "system_prompt": "تو ایجنت Z.ai هستی. وظیفه‌ات بررسی نهایی، تست سناریوها و تایید کیفیت کار بقیه ربات‌هاست."
    },
    #"Ollama_Llama": {
       # "role": "پردازشگر محلی، آفلاین و امنیتی روی سیستم",
      #  "system_prompt": "تو مدل Llama هستی که روی سیستم کاربر اجرا می‌شوی. وظیفه‌ات پردازش‌های محلی و چک کردن امینت داده‌هاست."
    #}
}

# =============================================================
# ۳. هسته مرکزی سرور MCP (Model Context Protocol)
# =============================================================
class MCPServer:
    def __init__(self):
        self.context_history = []

    def log_and_print(self, sender, role, content):
        """ذخیره پیام در زمینه مشترک و نمایش در ترمینال"""
        self.context_history.append({"sender": sender, "role": role, "content": content})
        print(f"\n🤖 [{sender} - {role}]:")
        print(f"💬 {content}")
        print("-" * 65)

    def call_bot_api(self, bot_name, prompt):
        """مدیریت درخواست‌ها و فراخوانی API ربات‌ها"""
        try:
            # ۱. فراخوانی Google Gemini
            if bot_name == "Gemini":
                if not gemini_client:
                    return "[Gemini]: کلید API تنظیم نشده است."
                res = gemini_client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                return res.text

            # ۲. فراخوانی Groq API (فوق‌سریع)
            elif bot_name == "Groq":
                headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
                data = {
                    "model": "llama-3.3-70b-versatile",
                    "messages": [{"role": "user", "content": prompt}]
                }
                res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=15)
                return res.json()['choices'][0]['message']['content']

            # ۳. فراخوانی DeepSeek API
            elif bot_name == "DeepSeek":
                headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}", "Content-Type": "application/json"}
                data = {
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": prompt}]
                }
                res = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=data, timeout=15)
                return res.json()['choices'][0]['message']['content']

            # ۴. فراخوانی OpenRouter API
            elif bot_name == "OpenRouter":
                headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
                data = {
                    "model": "google/gemini-2.0-flash-exp:free", # یا هر مدل رایگان دیگر در OpenRouter
                    "messages": [{"role": "user", "content": prompt}]
                }
                res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data, timeout=15)
                return res.json()['choices'][0]['message']['content']

            # ۵. فراخوانی GapGPT API
            elif bot_name == "GapGPT":
                headers = {"Authorization": f"Bearer {GAPGPT_API_KEY}", "Content-Type": "application/json"}
                data = {
                    "model": "gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": prompt}]
                }
                res = requests.post("https://api.gapgpt.app/v1/chat/completions", headers=headers, json=data, timeout=15)
                return res.json()['choices'][0]['message']['content']

            # ۶. فراخوانی Z.ai API
            elif bot_name == "Z.ai":
                headers = {"Authorization": f"Bearer {ZAI_API_KEY}", "Content-Type": "application/json"}
                data = {
                    "messages": [{"role": "user", "content": prompt}]
                }
                res = requests.post("https://api.z.ai/v1/chat/completions", headers=headers, json=data, timeout=15)
                return res.json()['choices'][0]['message']['content']

            # ۷. فراخوانی محلی Ollama (Llama) روی سیستم خودت
           # elif bot_name == "Ollama_Llama":
                #data = {
                   #
                   # "model": "llama3",
                  #  "prompt": prompt,
                 #   "stream": False
                #}
               # res = requests.post(OLLAMA_URL, json=data, timeout=30)
              #  return res.json()['response']

        except Exception as e:
            return f"❌ [خطا در اتصال به {bot_name}]: {str(e)}"

    def start_workflow(self, user_prompt):
        """شروع جلسه و هم‌افزایی تیم ربات‌ها"""
        print("==========================================================")
        print(f"🚀 پروژه جدید در سرور MCP شروع شد:\n📌 {user_prompt}")
        print("==========================================================")

        # ثبت ورود کارفرما
        self.log_and_print("User", "کارفرما", user_prompt)

        # چرخه ارسال پیام‌ها بین ربات‌ها
        for bot_name, bot_info in BOTS.items():
            # ساخت تاریخچه مشترک برای هماهنگی کامل ایجنت‌ها
            full_context = f"دستورالعمل اصلی نقش تو: {bot_info['system_prompt']}\n\nتاریخچه جلسه تا این لحظه:\n"
            for msg in self.context_history:
                full_context += f"- [{msg['sender']}]: {msg['content']}\n"
           
            full_context += f"\nنوبت توست ({bot_name}). بر اساس نقش خودت، نظر و بخش مربوطه را اضافه کن:"

            # دریافت پاسخ از ربات مربوطه
            response = self.call_bot_api(bot_name, full_context)
            self.log_and_print(bot_name, bot_info['role'], response)

        print("\n✅ پروژه با همکاری تمامی ایجنت‌های MCP با موفقیت تکمیل شد!")

# =============================================================
# ۴. اجرای سرور
# =============================================================
if __name__ == "__main__":
    mcp_hub = MCPServer()
   
    # دستور یا ایده پروژه را اینجا بنویس
    project_prompt = "طراحی و پیاده‌سازی یک ربات مدیریت امور روزانه با قابلیت یادآوری به زبان فارسی"
    mcp_hub.start_workflow(project_prompt)