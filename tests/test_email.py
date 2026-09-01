import smtplib

from email.message import EmailMessage

from src.config import (
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECEIVER,
)


def send_test_email():
    """Send a simple test email."""

    message = EmailMessage()

    message["Subject"] = "EMA Alert System - Test"
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER

    message.set_content(
        "Congratulations! Your EMA Alert System email "
        "notification is working successfully."
    )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            EMAIL_SENDER,
            EMAIL_PASSWORD
        )

        smtp.send_message(message)

    print("Test email sent successfully!")


if __name__ == "__main__":
    try:
        send_test_email()

    except Exception as error:
        print(f"Email error: {error}")