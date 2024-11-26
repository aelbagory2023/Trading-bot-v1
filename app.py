from flask import Flask, jsonify, request
from utils.portfolio_history import get_account_portfolio_history

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

if __name__ == '__main__':
    app.run(debug=True)
