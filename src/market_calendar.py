from datetime import datetime


NSE_HOLIDAYS_2026 = {
    "2026-01-26",  # Republic Day
    "2026-03-03",  # Holi
    "2026-03-26",  # Ram Navami
    "2026-03-31",  # Mahavir Jayanti
    "2026-04-03",  # Good Friday
    "2026-04-14",  # Dr. Babasaheb Ambedkar Jayanti
    "2026-05-01",  # Maharashtra Day
    "2026-05-28",  # Bakri Id
    "2026-06-26",  # Muharram
    "2026-09-14",  # Ganesh Chaturthi
    "2026-10-02",  # Mahatma Gandhi Jayanti
    "2026-10-20",  # Dussehra
    "2026-11-10",  # Diwali Balipratipada
    "2026-11-24",  # Guru Nanak Jayanti
    "2026-12-25",  # Christmas
}


def is_weekend():
    """Return True if today is Saturday or Sunday."""

    return datetime.now().weekday() >= 5


def is_market_holiday():
    """Return True if today is an NSE trading holiday."""

    today = datetime.now().strftime("%Y-%m-%d")

    return today in NSE_HOLIDAYS_2026


def is_market_closed_today():
    """Return True if the market is closed today."""

    return is_weekend() or is_market_holiday()