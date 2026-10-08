import imaplib
import email

# اطلاعات اتصال به سرور ایمیل
mail_server = 'imap.example.com'
username = 'your_email@example.com'
password = 'your_password'

# اتصال به سرور ایمیل
mail = imaplib.IMAP4_SSL(mail_server)
mail.login(username, password)

# انتخاب پوشه
mail.select('inbox')

# جستجوی ایمیل‌های جدید
status, messages = mail.search(None, 'UNSEEN')

# پردازش ایمیل‌ها
for msg_id in messages[0].split():
    response, msg_data = mail.fetch(msg_id, '(RFC822)')
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    # دریافت فرستنده و موضوع
    sender = msg['from']
    subject = msg['subject']

    print(f'ایمیل از: {sender}')
    print(f'موضوع: {subject}')

    # ارسال پاسخ خودکار
    # ... (کد ارسال ایمیل) ...

mail.close()
mail.logout()