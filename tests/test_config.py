from src.config import (
    TIMEFRAME,
    EMA_FAST,
    EMA_SLOW,
    SYMBOL,
    PERIOD,
    MARKET_START,
    MARKET_END,
)


def main():
    print("Configuration loaded successfully!")

    print(f"Symbol: {SYMBOL}")
    print(f"Timeframe: {TIMEFRAME}")
    print(f"Period: {PERIOD}")
    print(f"EMA Fast: {EMA_FAST}")
    print(f"EMA Slow: {EMA_SLOW}")
    print(f"Market Start: {MARKET_START}")
    print(f"Market End: {MARKET_END}")


if __name__ == "__main__":
    main()