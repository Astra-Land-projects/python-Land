import json
import os
from datetime import datetime

DATA_FILE = "school_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"tasks": [], "exams": []}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def show_menu():
    print("\n" + "="*40)
    print("🎒 مدرسه‌ی من")
    print("="*40)
    print("1. اضافه کردن کار")
    print("2. نمایش کارها")
    print("3. حذف کار")
    print("4. اضافه کردن امتحان")
    print("5. نمایش امتحان‌ها")
    print("6. خروج")
    print("="*40)

def add_task(data):
    task = input("📝 متن کار: ")
    data["tasks"].append({"text": task, "done": False})
    save_data(data)
    print("✅ اضافه شد!")

def show_tasks(data):
    if not data["tasks"]:
        print("📭 هیچ کاری نداری!")
        return
    for i, task in enumerate(data["tasks"], 1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}. {status} {task['text']}")

def delete_task(data):
    show_tasks(data)
    try:
        idx = int(input("شماره کار برای حذف: ")) - 1
        if 0 <= idx < len(data["tasks"]):
            removed = data["tasks"].pop(idx)
            save_data(data)
            print(f"🗑️ حذف شد: {removed['text']}")
        else:
            print("❌ شماره نامعتبر!")
    except ValueError:
        print("❌ لطفاً عدد وارد کن!")

def add_exam(data):
    subject = input("📚 اسم درس: ")
    date = input("📅 تاریخ امتحان (مثلاً 1404-10-15): ")
    data["exams"].append({"subject": subject, "date": date})
    save_data(data)
    print("✅ اضافه شد!")

def show_exams(data):
    if not data["exams"]:
        print("📭 هیچ امتحانی نداری!")
        return
    print("\n📚 امتحان‌ها:")
    for i, exam in enumerate(data["exams"], 1):
        print(f"{i}. {exam['subject']} — {exam['date']}")

def main():
    data = load_data()
    while True:
        show_menu()
        choice = input("انتخاب کن: ")
        if choice == "1":
            add_task(data)
        elif choice == "2":
            show_tasks(data)
        elif choice == "3":
            delete_task(data)
        elif choice == "4":
            add_exam(data)
        elif choice == "5":
            show_exams(data)
        elif choice == "6":
            print("👋 خدا حافظ!")
            break
        else:
            print("❌ انتخاب نامعتبر!")

if __name__ == "__main__":
    main()