import smtplib

from email.message import EmailMessage

from src.config import (
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECEIVER,
)


def send_alert(signal, candle_time, close_price):
    """Send EMA crossover alert email."""

    message = EmailMessage()

    message["Subject"] = f"NIFTY EMA Alert - {signal}"
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER

    message.set_content(
        f"""
EMA CROSSOVER DETECTED

Symbol: NIFTY
Signal: {signal}

Candle Time: {candle_time}
Close Price: {close_price}

EMA 9 and EMA 21 crossover detected.
"""
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

    print(f"Email alert sent: {signal}")