from config import ALPACA_CONFIG
from datetime import datetime
from lumibot.strategies import Strategy
from lumibot.traders import Trader
from lumibot.brokers import Alpaca
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import requests
from dotenv import load_dotenv

client = TradingClient(ALPACA_CONFIG['API_KEY'], ALPACA_CONFIG['API_SECRET'], paper=True)

ALPACA_API_URL = "https://paper-api.alpaca.markets/v2"

class MomentumTrading(Strategy):
    def initialize(self):
        self.sleeptime = "1D"
        self.stop_loss_pct = 0.05  # 5% stop loss
        self.take_profit_pct = 0.10  # 10% take profit
        self.symbols = ["BONK"]  # Add your desired symbols here

    def on_trading_iteration(self):
        for symbol in self.symbols:
            # Fetch the latest bars for the symbol
            data = self.fetch_latest_bars(symbol)
            if data:
                price = data['close'][-1]  # Get the latest closing price
                previous_price = data['close'][-2]  # Get the previous closing price

                # Determine momentum
                if price > previous_price:  # Upward momentum
                    quantity = self.cash / price
                    order = self.create_order(symbol, quantity, "buy")
                    self.submit_order(order)
                    self.set_stop_loss(symbol, price)
                    self.set_take_profit(symbol, price)
                elif price < previous_price:  # Downward momentum
                    # Implement a short sell if your strategy allows it
                    quantity = self.cash / price
                    order = self.create_order(symbol, quantity, "sell")
                    self.submit_order(order)
                    self.set_stop_loss(symbol, price)
                    self.set_take_profit(symbol, price)

    def fetch_latest_bars(self, symbol):
        url = f"https://data.alpaca.markets/v1beta3/crypto/us/latest/bars?symbols=BONK/USD"
        
        headers = {
            "accept": "application/json",
           
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()[symbol]
        else:
            print(f"Error fetching latest bars for {symbol}: {response.text}")
            return None

    def set_stop_loss(self, symbol, entry_price):
        stop_loss_price = entry_price * (1 - self.stop_loss_pct)
        stop_loss_order = CreateOrderRequest(
            symbol=symbol,
            qty=1,  # Adjust quantity as needed
            side=OrderSide.SELL,
            type='stop_limit',
            stop_price=stop_loss_price,
            limit_price=stop_loss_price,
            time_in_force=TimeInForce.GTC
        )
        self.submit_order(stop_loss_order)

    def set_take_profit(self, symbol, entry_price):
        take_profit_price = entry_price * (1 + self.take_profit_pct)
        take_profit_order = CreateOrderRequest(
            symbol=symbol,
            qty=1,  # Adjust quantity as needed
            side=OrderSide.SELL,
            type='limit',
            limit_price=take_profit_price,
            time_in_force=TimeInForce.GTC
        )
        self.submit_order(take_profit_order)

if __name__ == "__main__":
    trade = True  # Set to True to run live trading
    if trade:
        broker = Alpaca(ALPACA_CONFIG)
        strategy = MomentumTrading(broker=broker)
        trader = Trader()
        trader.add_strategy(strategy)
        trader.run_all()
    else:
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 11, 26)
        backtest = YahooBacktest(MomentumTrading(), start=start_date, end=end_date)
        backtest.run()
