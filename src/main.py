import time
from datetime import datetime, timedelta

from src.yahoo_data import fetch_data
from src.ema_calculator import calculate_ema
from src.crossover_detector import detect_crossover
from src.email_alert import send_alert
from src.alert_state import (
    get_last_alert,
    save_last_alert,
)
from src.config import (
    MARKET_START,
    MARKET_END,
)
from src.market_calendar import (
    is_weekend,
    is_market_holiday,
)


def is_market_time():
    """Check whether the current time is inside the monitoring window."""

    current_time = datetime.now().time()

    start_time = datetime.strptime(
        MARKET_START,
        "%H:%M"
    ).time()

    end_time = datetime.strptime(
        MARKET_END,
        "%H:%M"
    ).time()

    return start_time <= current_time <= end_time


def is_trading_day(date):
    """Return True if the given date is a trading day."""

    if date.weekday() >= 5:
        return False

    date_string = date.strftime("%Y-%m-%d")

    from src.market_calendar import NSE_HOLIDAYS_2026

    if date_string in NSE_HOLIDAYS_2026:
        return False

    return True


def get_next_trading_day():
    """Find the next valid trading day."""

    next_day = datetime.now().date() + timedelta(days=1)

    while not is_trading_day(next_day):
        next_day += timedelta(days=1)

    return next_day


def seconds_until_next_session():
    """Calculate seconds until the next market monitoring session."""

    now = datetime.now()

    market_start_time = datetime.strptime(
        MARKET_START,
        "%H:%M"
    ).time()

    market_end_time = datetime.strptime(
        MARKET_END,
        "%H:%M"
    ).time()

    today = now.date()

    # Before market start on a valid trading day
    if (
        is_trading_day(today)
        and now.time() < market_start_time
    ):
        next_session = datetime.combine(
            today,
            market_start_time
        )

    else:
        # After market close or non-trading day
        next_trading_day = get_next_trading_day()

        next_session = datetime.combine(
            next_trading_day,
            market_start_time
        )

    seconds = (
        next_session - now
    ).total_seconds()

    return max(int(seconds), 1)


def check_market():
    """Fetch data and check for a new EMA crossover."""

    print("\n" + "=" * 50)
    print(f"Checking market: {datetime.now()}")
    print("=" * 50)

    data = fetch_data()

    data = calculate_ema(data)

    signal, current_candle = detect_crossover(data)

    if signal:
        candle_time = str(current_candle.name)

        last_alert = get_last_alert()

        if candle_time == last_alert:
            print(
                "Crossover already alerted for candle: "
                f"{candle_time}"
            )
            return

        print(f"Crossover detected: {signal}")

        send_alert(
            signal=signal,
            candle_time=candle_time,
            close_price=current_candle["Close"]
        )

        save_last_alert(candle_time)

    else:
        print("No new crossover detected.")


def seconds_until_next_check():
    """Calculate seconds until the next 5-minute candle check."""

    now = datetime.now()

    minutes_until_next = 5 - (now.minute % 5)

    seconds = (
        minutes_until_next * 60
        - now.second
        + 10
    )

    return max(seconds, 1)


def main():
    """Run the EMA alert system during trading sessions."""

    print("EMA Alert System started.")

    print(
        f"Monitoring from {MARKET_START} "
        f"to {MARKET_END}."
    )

    print("Weekend and NSE holiday protection enabled.")
    print("Press Ctrl+C to stop.")

    while True:

        if is_trading_day(datetime.now().date()):

            if is_market_time():

                try:
                    check_market()

                except Exception as error:
                    print(f"Market check error: {error}")

                wait_seconds = seconds_until_next_check()

                print(
                    f"Waiting {wait_seconds} seconds "
                    "until next candle check..."
                )

                time.sleep(wait_seconds)

            else:

                wait_seconds = seconds_until_next_session()

                wait_hours = round(
                    wait_seconds / 3600,
                    2
                )

                print(
                    "\nOutside monitoring hours."
                )

                print(
                    f"Sleeping for approximately "
                    f"{wait_hours} hours until "
                    "the next market session."
                )

                time.sleep(wait_seconds)

        else:

            wait_seconds = seconds_until_next_session()

            next_day = get_next_trading_day()

            wait_hours = round(
                wait_seconds / 3600,
                2
            )

            print(
                "\nMarket is closed today "
                "(weekend or holiday)."
            )

            print(
                f"Next trading day: {next_day}"
            )

            print(
                f"Sleeping for approximately "
                f"{wait_hours} hours."
            )

            time.sleep(wait_seconds)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nEMA Alert System stopped.")