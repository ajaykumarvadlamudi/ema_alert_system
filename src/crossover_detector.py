from src.ema_calculator import calculate_ema
from src.yahoo_data import fetch_data
from src.email_alert import send_alert


def detect_crossover(data):
    """Detect EMA bullish or bearish crossover."""

    # Ignore the currently forming candle
    closed_data = data.iloc[:-1].copy()

    # We need at least two closed candles
    if len(closed_data) < 2:
        return None, None

    previous = closed_data.iloc[-2]
    current = closed_data.iloc[-1]

    previous_fast = previous["EMA_FAST"]
    previous_slow = previous["EMA_SLOW"]

    current_fast = current["EMA_FAST"]
    current_slow = current["EMA_SLOW"]

    # Bullish crossover
    if previous_fast <= previous_slow and current_fast > current_slow:
        return "BULLISH", current

    # Bearish crossover
    if previous_fast >= previous_slow and current_fast < current_slow:
        return "BEARISH", current

    # No crossover
    return None, None


if __name__ == "__main__":
    try:
        data = fetch_data()

        data = calculate_ema(data)

        signal, current_candle = detect_crossover(data)

        if signal:
            print(f"\nCrossover detected: {signal}")

            send_alert(
                signal=signal,
                candle_time=current_candle.name,
                close_price=current_candle["Close"]
            )

        else:
            print("\nNo new crossover detected.")

    except Exception as error:
        print(f"Error: {error}")