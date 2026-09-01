# EMA Alert System

A Python-based market monitoring system that detects EMA crossovers and sends email alerts.

## Features

- Fetches NIFTY data using Yahoo Finance
- Uses 5-minute candles
- Calculates EMA 9 and EMA 21
- Detects bullish and bearish crossovers
- Sends email alerts
- Prevents duplicate alerts
- Monitors configured market hours
- Includes weekend and holiday protection

## Technology

- Python
- pandas
- yfinance
- python-dotenv

## Run the application

```powershell
python -m src.main