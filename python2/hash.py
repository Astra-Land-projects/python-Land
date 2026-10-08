import hashlib

# دیکشنری از کلمات معروف ناتو (آلفا، براوو و...) و هش SHA-256 آن‌ها
# در واقعیت، ما این هش‌ها را از قبل محاسبه کرده و ذخیره می‌کنیم.
known_hashes = {
    hashlib.sha256("alpha".encode()).hexdigest(): "alpha",
    hashlib.sha256("bravo".encode()).hexdigest(): "bravo",
    hashlib.sha256("charlie".encode()).hexdigest(): "charlie",
    # می‌توانید کلمات بیشتری اضافه کنید
}

def find_message_from_hash(hash_input):
    """
    بررسی می‌کند که آیا هش ورودی در لیست هش‌های شناخته شده وجود دارد یا خیر.
    """
    # هش ورودی را محاسبه می‌کنیم (اگر ورودی متن باشد) یا مستقیماً از آن استفاده می‌کنیم
    if len(hash_input) == 64:  # طول هش SHA-256
        search_hash = hash_input.lower()
    else:
        search_hash = hashlib.sha256(hash_input.encode()).hexdigest()
   
    # جستجو در دیکشنری
    if search_hash in known_hashes:
        return known_hashes[search_hash]
    else:
        return None

# --- اجرای پروژه ---
# فرض کنید ما یک هش دریافت کرده‌ایم (مثلاً هش کلمه "bravo")
# هش واقعی کلمه "bravo" را محاسبه می‌کنیم:
bravo_hash = hashlib.sha256("bravo".encode()).hexdigest()

print(f"hash word 'bravo': {bravo_hash}")

# حالا سعی می‌کنیم پیام را از روی این هش استخراج کنیم
extracted_message = find_message_from_hash(bravo_hash)

if extracted_message:
    print(f"✅ message was extraction: {extracted_message}")
else:
    print("❌ message with hash not find in the list.")

# تست با متن "alpha"
alpha_hash = hashlib.sha256("alpha".encode()).hexdigest()
extracted_alpha = find_message_from_hash(alpha_hash)
print(f"hash 'alpha' -> message was extraction: {extracted_alpha}")