import json
import os
from datetime import datetime

DATA_FILE = "notes_data.json"

def load_notes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

def show_menu():
    print("\n" + "="*40)
    print("📝 یادداشت‌بردار")
    print("="*40)
    print("1. نوشتن یادداشت جدید")
    print("2. نمایش همه یادداشت‌ها")
    print("3. حذف یادداشت")
    print("4. خروج")
    print("="*40)

def add_note(notes):
    text = input("✏️ متن یادداشت: ")
    note = {
        "text": text,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    notes.append(note)
    save_notes(notes)
    print("✅ یادداشت ذخیره شد!")

def show_notes(notes):
    if not notes:
        print("📭 هنوز یادداشتی نداری!")
        return
    print("\n📋 یادداشت‌های تو:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. [{note['date']}] {note['text']}")

def delete_note(notes):
    show_notes(notes)
    if not notes:
        return
    try:
        idx = int(input("🔢 شماره یادداشت برای حذف: ")) - 1
        if 0 <= idx < len(notes):
            removed = notes.pop(idx)
            save_notes(notes)
            print(f"🗑️ یادداشت حذف شد: {removed['text']}")
        else:
            print("❌ شماره اشتباهه!")
    except ValueError:
        print("❌ لطفاً عدد وارد کن!")

def main():
    notes = load_notes()
    while True:
        show_menu()
        choice = input("🔢 انتخاب کن: ")
        if choice == "1":
            add_note(notes)
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            print("👋 خداحافظ!")
            break
        else:
            print("❌ گزینه نامعتبر!")

if __name__ == "__main__":
    main()
```

---

## 📝 پروژه سوم: «ماشین‌حساب» (با پایتون)

```python
# calculator.py
import math

def show_menu():
    print("\n" + "="*40)
    print("🧮 ماشین‌حساب")
    print("="*40)
    print("1. جمع (+)")
    print("2. تفریق (-)")
    print("3. ضرب (*)")
    print("4. تقسیم (/)")
    print("5. توان (^)")
    print("6. جذر (√)")
    print("7. خروج")
    print("="*40)

def get_number(prompt="🔢 عدد وارد کن: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ لطفاً عدد معتبر وارد کن!")

def main():
    while True:
        show_menu()
        choice = input("🔢 انتخاب کن: ")
       
        if choice == "1":
            a = get_number("عدد اول: ")
            b = get_number("عدد دوم: ")
            print(f"✅ نتیجه: {a} + {b} = {