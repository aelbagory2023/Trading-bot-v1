import axios from 'axios';
import dotenv from 'dotenv';
import requests
import os

load_dotenv()


ALPACA_API_URL = 'https://data.alpaca.markets/v1beta3/crypto';
ALPACA_API_KEY = ALPACA_CONFIG['API_KEY']
ALPACA_SECRET_KEY = ALPACA_CONFIG['API_SECRET']

print(ALPACA_API_KEY)
print(ALPACA_SECRET_KEY)


def fetch_historical_bars(loc, symbols, timeframe='1Min', limit=1000, sort='asc'):
    """Fetch historical bars for a list of crypto symbols."""
    url = f"{ALPACA_API_URL}/{loc}/bars"
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
    }
    params = {
        'symbols': symbols,
        'timeframe': timeframe,
        'limit': limit,
        'sort': sort
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical bars: {e}")
        return {"error": str(e)}

def fetch_latest_bars(loc, symbols):
    """Fetch the latest bars for a list of crypto symbols."""
    url = f"{ALPACA_API_URL}/{loc}/latest/bars"
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
    }
    params = {
        'symbols': symbols
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest bars: {e}")
        return {"error": str(e)}

def fetch_latest_order_book(loc, symbols):
    """Fetch the latest order book for a list of crypto symbols."""
    url = f"{ALPACA_API_URL}/{loc}/latest/orderbooks"
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
    }
    params = {
        'symbols': symbols
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest order book: {e}")
        return {"error": str(e)}

def fetch_latest_quotes(loc, symbols):
    """Fetch the latest quotes for a list of crypto symbols."""
    url = f"{ALPACA_API_URL}/{loc}/latest/quotes"
    headers = {
        "accept": "application/json",
            "APCA-API-KEY-ID": ALPACA_API_KEY,
            "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
    }
    params = {
        'symbols': symbols
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest quotes: {e}")
        return {"error": str(e)}

def fetch_latest_trades(loc, symbols):
    """Fetch the latest trades for a list of crypto symbols."""
    url = f"{ALPACA_API_URL}/{loc}/latest/trades"
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
    }
    params = {
        'symbols': symbols
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest trades: {e}")
        return {"error": str(e)}

def fetch_historical_quotes(loc, symbols, start_date, end_date):
    """Fetch historical quotes for a list of crypto symbols."""
    url = f"{ALPACA_API_URL}/{loc}/quotes"
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
    }
    params = {
        'symbols': symbols,
        'start': start_date,
        'end': end_date
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical quotes: {e}")
        return {"error": str(e)}

def fetch_snapshots(loc, symbols):
    """Fetch snapshots for a list of crypto symbols."""
    url = f"{ALPACA_API_URL}/{loc}/snapshots"
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
    }
    params = {
        'symbols': symbols
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching snapshots: {e}")
        return {"error": str(e)}

def fetch_historical_trades(loc, symbols, start_date, end_date):
    """Fetch historical trades for a list of crypto symbols."""
    url = f"{ALPACA_API_URL}/{loc}/trades"
    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
    }
    params = {
        'symbols': symbols,
        'start': start_date,
        'end': end_date
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical trades: {e}")
        return {"error": str(e)}

export { 
  fetchHistoricalBars, 
  fetchLatestBars, 
  fetchLatestOrderBook, 
  fetchLatestQuotes, 
  fetchLatestTrades, 
  fetchHistoricalQuotes, 
  fetchSnapshots, 
  fetchHistoricalTrades 
};