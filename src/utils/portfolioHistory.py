import requests

def get_account_portfolio_history(api_key_id, api_secret_key, start_date=None, end_date=None):
    """
    # Fetches the account portfolio history from the Alpaca API.

    # Parameters:
    # - api_key_id: Your Alpaca API key ID.
    # - api_secret_key: Your Alpaca API secret key.
    # - start_date: Optional start date for the timespan (YYYY-MM-DD).
    # - end_date: Optional end date for the timespan (YYYY-MM-DD).

    # Returns:
    # - A dictionary containing the portfolio history data or an error message.
    # """
    url = "https://paper-api.alpaca.markets/v2/account/portfolio/history"
    headers = {
        "APCA_API_KEY_ID": api_key_id,
        "APCA_API_SECRET_KEY": api_secret_key,
        "Content-Type": "application/json"
    }

    # Prepare parameters for the request
    params = {}
    if start_date:
        params['start'] = start_date
    if end_date:
        params['end'] = end_date

    try:
        # Make the request to the Alpaca API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data from the response
    except requests.exceptions.RequestException as e:
        return {"error": str(e), "status_code": response.status_code if response else None}
