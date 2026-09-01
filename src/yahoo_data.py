import yfinance as yf

from src.config import SYMBOL, TIMEFRAME, PERIOD

def fetch_data():
    """Fetch recent market data from Yahoo Finance."""

    print(f"Fetching {TIMEFRAME} data for {SYMBOL}...")
    ticker = yf.Ticker(SYMBOL)

    data = ticker.history(
        period=PERIOD,
        interval=TIMEFRAME
    )

    if data.empty:
        raise ValueError(
            f"No data received for {SYMBOL}. "
            "Check the symbol or Yahoo Finance availability."
        )

    return data

if __name__ == "__main__":
    try:
        data = fetch_data()
        print("\nData fetched successfully!")
        print(f"Total candles: {len(data)}")

        print("\nLast 10 candles:")
        print(data.tail(10))

    except Exception as error:
        print(f"Yahoo Finance error: {error}")
