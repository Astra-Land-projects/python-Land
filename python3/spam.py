#!/usr/bin/env python3
"""
تشخیص اسپم - مینی پروژه هوش مصنوعی
=====================================
یک دسته‌بند ساده اسپم/غیراسپم با الگوریتم Naive Bayes که کاملاً از صفر
نوشته شده (بدون نیاز به کتابخانه‌های سنگین مثل sklearn یا tensorflow).

فقط با کتابخانه استاندارد پایتون کار می‌کنه، پس روی هر گوشی/ترموکسی
بدون نصب اضافه اجرا میشه.

نحوه کار:
    1. یک مجموعه پیام‌های نمونه (اسپم و غیراسپم) به مدل داده میشه.
    2. مدل یاد می‌گیره کدوم کلمات بیشتر توی اسپم‌ها میان.
    3. برای پیام جدید، احتمال اسپم بودنش رو حساب می‌کنه.
"""

import re
import math
from collections import defaultdict


class SpamDetector:
    """یک دسته‌بند Naive Bayes ساده برای تشخیص اسپم."""

    def __init__(self):
        self.spam_word_counts = defaultdict(int)
        self.ham_word_counts = defaultdict(int)
        self.spam_count = 0
        self.ham_count = 0
        self.vocab = set()

    @staticmethod
    def tokenize(text: str) -> list[str]:
        """متن رو به کلمات کوچک (lowercase) تبدیل می‌کنه."""
        text = text.lower()
        words = re.findall(r"[a-zA-Z\u0600-\u06FF]+", text)
        return words

    def train(self, messages: list[tuple[str, str]]):
        """
        مدل رو با لیستی از (متن پیام، برچسب) آموزش می‌ده.
        برچسب باید 'spam' یا 'ham' باشه.
        """
        for text, label in messages:
            words = self.tokenize(text)
            self.vocab.update(words)

            if label == "spam":
                self.spam_count += 1
                for w in words:
                    self.spam_word_counts[w] += 1
            else:
                self.ham_count += 1
                for w in words:
                    self.ham_word_counts[w] += 1

    def predict(self, text: str) -> tuple[str, float]:
        """
        برای یک پیام جدید، برچسب پیش‌بینی‌شده و احتمال اسپم بودن رو برمی‌گردونه.
        از لگاریتم احتمال استفاده می‌کنیم تا دقت عددی حفظ بشه.
        """
        words = self.tokenize(text)
        total_docs = self.spam_count + self.ham_count
        if total_docs == 0:
            raise ValueError("مدل هنوز آموزش ندیده! اول train() رو صدا بزن.")

        # احتمال پیشین (prior)
        log_prob_spam = math.log(self.spam_count / total_docs)
        log_prob_ham = math.log(self.ham_count / total_docs)

        vocab_size = len(self.vocab)
        total_spam_words = sum(self.spam_word_counts.values())
        total_ham_words = sum(self.ham_word_counts.values())

        for w in words:
            # Laplace smoothing تا کلمات جدید احتمال صفر نگیرن
            spam_wc = self.spam_word_counts.get(w, 0)
            ham_wc = self.ham_word_counts.get(w, 0)

            log_prob_spam += math.log((spam_wc + 1) / (total_spam_words + vocab_size))
            log_prob_ham += math.log((ham_wc + 1) / (total_ham_words + vocab_size))

        # تبدیل لگاریتم به احتمال نرمال‌شده برای نمایش بهتر
        max_log = max(log_prob_spam, log_prob_ham)
        spam_exp = math.exp(log_prob_spam - max_log)
        ham_exp = math.exp(log_prob_ham - max_log)
        spam_probability = spam_exp / (spam_exp + ham_exp)

        label = "spam" if log_prob_spam > log_prob_ham else "ham"
        return label, spam_probability


# ---------------------------------------------------------------------------
# داده‌ی آموزشی نمونه (کوچک، فقط برای دمو - می‌تونی بزرگترش کنی)
# ---------------------------------------------------------------------------
TRAINING_DATA = [
    ("برنده جایزه یک میلیونی شدید همین الان کلیک کنید", "spam"),
    ("تخفیف ویژه فقط امروز خرید کنید و برنده شوید", "spam"),
    ("وام فوری بدون ضامن همین حالا ثبت نام کنید", "spam"),
    ("شماره کارت خود را برای دریافت جایزه ارسال کنید", "spam"),
    ("این پیام رایگان است برنده قرعه کشی شدید", "spam"),
    ("کلیک کنید و آیفون رایگان دریافت کنید همین امروز", "spam"),
    ("سلام، جلسه فردا ساعت ده صبح برگزار می‌شود", "ham"),
    ("گزارش پروژه رو تا فردا برام بفرست لطفا", "ham"),
    ("سلام خوبی؟ کی وقت داری بریم بیرون", "ham"),
    ("فایل ضمیمه رو چک کن و نظرت رو بگو", "ham"),
    ("مامان امروز شام میایم خونه شما", "ham"),
    ("کتاب رو تموم کردم عالی بود پیشنهاد میکنم بخونی", "ham"),
    ("فردا کلاس تعطیله استاد اطلاع داد", "ham"),
    ("جایزه نقدی برای شما رزرو شده همین الان دریافت کنید", "spam"),
]


def main():
    print("=" * 55)
    print("  تشخیص اسپم - مینی پروژه هوش مصنوعی")
    print("=" * 55)
    print()

    # ساخت و آموزش مدل
    detector = SpamDetector()
    detector.train(TRAINING_DATA)
    print(f"مدل با {detector.spam_count} پیام اسپم و {detector.ham_count} پیام عادی آموزش دید.\n")

    # چند پیام تستی برای دمو
    test_messages = [
        "برنده جایزه شدید فورا کلیک کنید",
        "سلام فردا میای دانشگاه؟",
        "وام فوری و رایگان همین الان دریافت کنید",
        "گزارش کار امروز رو برات ایمیل کردم",
    ]

    print("نتایج تست:\n")
    for msg in test_messages:
        label, prob = detector.predict(msg)
        emoji = "🚫" if label == "spam" else "✅"
        print(f"{emoji} [{label.upper():4s}] ({prob*100:.1f}% اسپم)  →  {msg}")

    print()
    print("-" * 55)
    print("حالا خودت امتحان کن (برای خروج، 'exit' بزن):")
    print("-" * 55)

    while True:
        try:
            user_input = input("\nپیام: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if user_input.lower() == "exit" or not user_input:
            break
        label, prob = detector.predict(user_input)
        emoji = "🚫" if label == "spam" else "✅"
        print(f"{emoji} نتیجه: {label.upper()}  (احتمال اسپم بودن: {prob*100:.1f}%)")


if __name__ == "__main__":
    main()