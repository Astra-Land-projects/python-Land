def encrypt_message(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # تعیین نقطه شروع (حروف کوچک یا بزرگ)
            start = ord('a') if char.islower() else ord('A')
            # محاسبه جابجایی و بازگشت به محدوده حروف الفبا
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt_message(text, shift):
    # رمزگشایی فقط یعنی جابجایی به سمت مخالف
    return encrypt_message(text, -shift)

# --- اجرای برنامه ---
message = input("Enter your message: ")
key = int(input("password number(example:3 password): "))

encrypted = encrypt_message(message, key)
decrypted = decrypt_message(encrypted, key)

print(f"\nmain message: {message}")
print(f"message have password: {encrypted}")
print(f"message have not password: {decrypted}")