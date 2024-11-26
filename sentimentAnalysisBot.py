import datetime, requests, yfinance as yf
from alpaca.trade_api.rest import REST
from getpass import getpass
import dotenv

dotenv.config();

ALPACA_API_URL = 'https://data.alpaca.markets/v1beta3/crypto';
ALPACA_API_KEY = process.env.ALPACA_API_KEY;
ALPACA_SECRET_KEY = process.env.ALPACA_SECRET_KEY;


print(news)

# Fetch news articles for ETH
url = "https://data.alpaca.markets/v1beta1/news?sort=desc&symbols=ETH"

headers = {
    "accept": "application/json",
    "alpaca_api_key": ALPACA_API_KEY,  # Use your API key variable
    "alpaca_secret_key": ALPACA_SECRET_KEY  # Use your secret key variable
}

response = requests.get(url, headers=headers)

print(response.text)