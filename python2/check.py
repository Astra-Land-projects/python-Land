import requests
import smtplib
from email.mime.text import MIMEText
import time

def check_website(url, email_sender, email_receiver, email_password):
    """Checks the uptime of a website and sends an email alert if it's down."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        print(f"{url} is up! Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{url} is down! Error: {e}")

        # Send email alert
        subject = f"{url} is Down!"
        body = f"The website {url} is currently down. Error: {e}"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = email_sender
        msg['To'] = email_receiver

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(email_sender, email_password)
                smtp.send_message(msg)
            print("Email alert sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

if __name__ == "__main__":
    website_url = "https://www.example.com"  # Replace with your website URL
    email_sender = "your_email@gmail.com"  # Replace with your email address
    email_password = "your_password"  # Replace with your email password (consider using an app password)
    email_receiver = "recipient_email@example.com"  # Replace with recipient email

    while True:
        check_website(website_url, email_sender, email_receiver, email_password)
        time.sleep(60 * 5)  # Check every 5 minutes