from pathlib import Path


STATE_FILE = Path(__file__).resolve().parent.parent / "alert_state.txt"


def get_last_alert():
    """Get the last alerted candle time."""

    if not STATE_FILE.exists():
        return None

    return STATE_FILE.read_text().strip()


def save_last_alert(candle_time):
    """Save the candle time of the last alert."""

    STATE_FILE.write_text(str(candle_time))