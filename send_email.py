import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv  # pip install python-dotenv

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
        server.starttls()  # Start TLS encryption
        print("Connection to SMTP server successful.")
except Exception as e:
    print(f"Failed to connect to SMTP server: {e}")


def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Rohan Rajput corp.", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        I hope you are well.
        I just wanted to drop you a quick note to remind you that {amount} USD in respect of our invoice {invoice_no} is due for payment on {due_date}.
        I would be really grateful if you could confirm that everything is on track for payment.
        Best regards
        YOUR NAME
        """
    )
    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hi {name},</p>
        <p>I hope you are well.</p>
        <p>I just wanted to drop you a quick note to remind you that <strong>{amount} USD</strong> in respect of our invoice {invoice_no} is due for payment on <strong>{due_date}</strong>.</p>
        <p>I would be really grateful if you could confirm that everything is on track for payment.</p>
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


if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        receiver_email="",  
        name="Rohan Rajput",
        due_date="12, Apr 2025",
        invoice_no="INV-21-12-009",
        amount="5",
    )