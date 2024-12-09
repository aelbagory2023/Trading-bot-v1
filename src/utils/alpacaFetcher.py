import axios from 'axios';
import dotenv from 'dotenv';
import requests
import os

load_dotenv()


ALPACA_API_URL = 'https://data.alpaca.markets/v1beta3/crypto';


https://data.alpaca.markets/v1beta3/crypto/us/bars?symbols=BTC%2FUSD&timeframe=1Min&limit=1000&sort=asc


def fetch_historical_bars(loc, symbols, timeframe='1Min', limit=1000, sort='asc'):
    """Fetch historical bars for a list of crypto symbols."""
    url = f"{ALPACA_API_URL}/{loc}/bars?symbols={symbols}%2FUSD&timeframe={timeframe}&limit=100&sort=asc"
    headers = {
        "accept": "application/json",
      
    }
    params = {
        'symbols': symbols,
        'loc': 'us',
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
    url = f"{ALPACA_API_URL}/{loc}/latest/bars?symbols={symbols}"
    headers = {
        "accept": "application/json",
       
    }
    params = {
        'symbols': symbols,
        'loc': 'us',
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
    url = f"{ALPACA_API_URL}/{loc}/latest/orderbooks?symbols={symbols}"
    headers = {
        "accept": "application/json",
       
    }
    params = {
        'symbols': symbols,
        'loc': 'us',
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
    url = f"{ALPACA_API_URL}/{loc}/latest/quotes?symbols={symbols}"
    headers = {
        "accept": "application/json",
           
    }
    params = {
        'symbols': symbols,
        'loc': 'us',
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
    url = f"{ALPACA_API_URL}/{loc}/latest/trades?symbols={symbols}"
    headers = {
        "accept": "application/json",
        
    }
    params = {
        'symbols': symbols,
        'loc': 'us',
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching latest trades: {e}")
        return {"error": str(e)}

def fetch_historical_quotes(loc, symbols, start_date, end_date):
    """Fetch historical quotes for a list of crypto symbols from the last 24 hours."""
    url = f"{ALPACA_API_URL}/{loc}/quotes?symbols={symbols}&start={start.strftime('%Y-%m-%dT%H:%M:%SZ')}&end={end.strftime('%Y-%m-%dT%H:%M:%SZ')}&limit=1000&sort=asc"
    headers = {
        "accept": "application/json",
       
    }
    # Calculate start and end dates for last 24 hours
    end = datetime.datetime.utcnow()
    start = end - datetime.timedelta(days=1)
    
    params = {
        'symbols': symbols,
        'loc': 'us',
        'start': start.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'end': end.strftime('%Y-%m-%dT%H:%M:%SZ'), 
        'limit': 1000,
        'sort': 'asc'
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
    url = f"{ALPACA_API_URL}/{loc}/snapshots?symbols={symbols}"
    headers = {
        "accept": "application/json",
    
    }
    params = {
        'symbols': symbols,
        'loc': 'us',
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
    # Calculate start and end dates for last 24 hours
    end = datetime.datetime.utcnow()
    start = end - datetime.timedelta(days=1)
    
    url = f"https://data.alpaca.markets/v1beta3/crypto/{loc}/trades?symbols={symbols}&start={start.strftime('%Y-%m-%dT%H:%M:%SZ')}&end={end.strftime('%Y-%m-%dT%H:%M:%SZ')}&limit=1000&sort=asc"
    headers = {
        "accept": "application/json",
       
    }
    params = {
        'symbols': symbols,
        'loc': 'us',
        'start': start_date,
        'end': end_date,
        'limit': 1000,
        'sort': 'asc'
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