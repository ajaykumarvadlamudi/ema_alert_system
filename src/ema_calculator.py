import pandas as pd

from src.config import EMA_FAST, EMA_SLOW


def calculate_ema(data):
    """Calculate EMA values using closing prices."""

    data = data.copy()

    data["EMA_FAST"] = (
        data["Close"]
        .ewm(span=EMA_FAST, adjust=False)
        .mean()
    )

    data["EMA_SLOW"] = (
        data["Close"]
        .ewm(span=EMA_SLOW, adjust=False)
        .mean()
    )

    return data


if __name__ == "__main__":
    from src.yahoo_data import fetch_data

    data = fetch_data()

    data = calculate_ema(data)

    # Ignore the currently forming candle
    closed_data = data.iloc[:-1]

    print("\nLast 5 closed candles with EMA values:")

    print(
        closed_data[
            ["Close", "EMA_FAST", "EMA_SLOW"]
        ].tail(5)
    )