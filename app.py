from flask import Flask, jsonify, request
from utils.portfolio_history import get_account_portfolio_history
from utils.alpaca_fetcher import (
    fetch_historical_bars,
    fetch_latest_bars,
    fetch_latest_order_book,
    fetch_latest_quotes,
    fetch_latest_trades,
    fetch_historical_quotes,
    fetch_snapshots,
    fetch_historical_trades
)

app = Flask(__name__)

@app.route('/api/account/portfolio/history', methods=['GET'])
def account_portfolio_history():
    api_key_id = "your_api_key_id"  # Replace with your API key
    api_secret_key = "your_api_secret_key"  # Replace with your API secret

    # Optional: Get query parameters for timespan
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Call the utility function
    portfolio_history = get_account_portfolio_history(api_key_id, api_secret_key, start_date, end_date)

    return jsonify(portfolio_history)

@app.route('/api/crypto/historical-bars', methods=['GET'])
def historical_bars():
    loc = request.args.get('loc', 'us')  # Default location to 'us'
    symbols = request.args.get('symbols')  # Comma-separated symbols
    timeframe = request.args.get('timeframe', '1Min')  # Default timeframe
    limit = request.args.get('limit', 1000)  # Default limit
    sort = request.args.get('sort', 'asc')  # Default sort order

    # Fetch historical bars using the utility function
    data = fetch_historical_bars(loc, symbols, timeframe, limit, sort)
    return jsonify(data)

@app.route('/api/crypto/latest-bars', methods=['GET'])
def latest_bars():
    loc = request.args.get('loc', 'us')  # Default location to 'us'
    symbols = request.args.get('symbols')  # Comma-separated symbols

    # Fetch latest bars using the utility function
    data = fetch_latest_bars(loc, symbols)
    return jsonify(data)

@app.route('/api/crypto/latest-orderbook', methods=['GET'])
def latest_order_book():
    loc = request.args.get('loc', 'us')  # Default location to 'us'
    symbols = request.args.get('symbols')  # Comma-separated symbols

    # Fetch latest order book using the utility function
    data = fetch_latest_order_book(loc, symbols)
    return jsonify(data)

@app.route('/api/crypto/latest-quotes', methods=['GET'])
def latest_quotes():
    loc = request.args.get('loc', 'us')  # Default location to 'us'
    symbols = request.args.get('symbols')  # Comma-separated symbols

    # Fetch latest quotes using the utility function
    data = fetch_latest_quotes(loc, symbols)
    return jsonify(data)

@app.route('/api/crypto/latest-trades', methods=['GET'])
def latest_trades():
    loc = request.args.get('loc', 'us')  # Default location to 'us'
    symbols = request.args.get('symbols')  # Comma-separated symbols

    # Fetch latest trades using the utility function
    data = fetch_latest_trades(loc, symbols)
    return jsonify(data)

@app.route('/api/crypto/historical-quotes', methods=['GET'])
def historical_quotes():
    loc = request.args.get('loc', 'us')  # Default location to 'us'
    symbols = request.args.get('symbols')  # Comma-separated symbols
    start_date = request.args.get('start_date')  # Start date for historical quotes
    end_date = request.args.get('end_date')  # End date for historical quotes

    # Fetch historical quotes using the utility function
    data = fetch_historical_quotes(loc, symbols, start_date, end_date)
    return jsonify(data)

@app.route('/api/crypto/snapshots', methods=['GET'])
def snapshots():
    loc = request.args.get('loc', 'us')  # Default location to 'us'
    symbols = request.args.get('symbols')  # Comma-separated symbols

    # Fetch snapshots using the utility function
    data = fetch_snapshots(loc, symbols)
    return jsonify(data)

@app.route('/api/crypto/historical-trades', methods=['GET'])
def historical_trades():
    loc = request.args.get('loc', 'us')  # Default location to 'us'
    symbols = request.args.get('symbols')  # Comma-separated symbols
    start_date = request.args.get('start_date')  # Start date for historical trades
    end_date = request.args.get('end_date')  # End date for historical trades

    # Fetch historical trades using the utility function
    data = fetch_historical_trades(loc, symbols, start_date, end_date)
    return jsonify(data)

# Other endpoints...

if __name__ == '__main__':
    app.run(debug=True)
