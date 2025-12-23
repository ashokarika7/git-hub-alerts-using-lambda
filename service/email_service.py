import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")
class EmailService:
    @staticmethod
    def send_email_task(user: str, repo: str, event_type: str):
        subject = f"🚀 GitHub Alert: {event_type} in {repo}"
        body = f"Hello!\n\nUser '{user}' just triggered a '{event_type}' event in your repository '{repo}'."

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.ehlo()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
                print(f"✅ Email sent successfully for {event_type}!")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")