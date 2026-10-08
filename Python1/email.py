def split_email(email):
    try:
        username, domain = email.split('@')
        return username, domain
    except ValueError:
        return None, None

# مثال استفاده
email = input("pls enter your email: ")
username, domain = split_email(email)

if username and domain:
    print(f"username: {username}")
    print(f"domain: {domain}")
else:
    print("address is not available.")