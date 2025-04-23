import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

EMAIL_SERVER = "smtp.gmail.com"
PORT = 587  # for TLS

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

print(f"Sender Email: {sender_email}, Password: {password_email}")
if not sender_email or not password_email:
    print("Environment variables are not loaded properly.")

try:
    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()  
        print("Connection to SMTP server successful.")
except Exception as e:
    print(f"Failed to connect to SMTP server: {e}")


def send_email(subject, receiver_email, name, due_date):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Email Automation JIIT corp.", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hi {name},</p>
        <p>I hope you are well.</p>
        <p>It is a reminder email for you from the JIIT corp. to drop you a quick note to {subject} completion on <strong>{due_date}</strong>.</p>
        <p>Otherwise you will be marked Late after the {due_date}</p>
        <p>Best regards</p>
        <p>YOUR NAME</p>
      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        try:
            server.login(sender_email, password_email)
            print("Login successful.")
        except smtplib.SMTPAuthenticationError as e:
            print("Authentication failed. Check your email and password.")
            print(f"Error code: {e.smtp_code}, Error message: {e.smtp_error}")
        except Exception as e:
            print("An error occurred while logging in:")
            print(e)
        server.sendmail(sender_email, receiver_email, msg.as_string())
