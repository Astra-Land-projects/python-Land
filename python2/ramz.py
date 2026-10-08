def caesar_cipher(text, shift):
    """
    متن رو با استفاده از رمزنگاری سزار رمزنگاری یا رمزگشایی می‌کنه.
    """
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result

# مثال استفاده
text = "hello world 123"
shift = 3

encrypted_text = caesar_cipher(text, shift)
print("password text:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("open password text:", decrypted_text)