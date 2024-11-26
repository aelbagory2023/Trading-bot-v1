from config import ALPACA_CONFIG
from datetime import datetime
from lumibot.strategies import Strategy
from lumibot.traders import Trader
from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooBacktest
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest, CreateOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


class BuyHold(Strategy):
    def initialize(self):
        self.sleeptime = "1D"
        self.stop_loss_pct = 0.05  # 5% stop loss
        self.take_profit_pct = 0.10  # 10% take profit

    def on_trading_iteration(self):
        if self.first_iteration:
            symbol = "BONK"
            price = self.get_last_price(symbol)
            quantity = self.cash / price
            
            # Create a buy order
            order = self.create_order(symbol, quantity, "buy")
            self.submit_order(order)

            # Set stop-loss and take-profit
            self.set_stop_loss(symbol, price)
            self.set_take_profit(symbol, price)

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
    trade = False
    if trade:
        broker = Alpaca(ALPACA_CONFIG)
        strategy = BuyHold(broker=broker)
        trader = Trader()
        trader.add_strategy(strategy)
        trader.run_all()
    else:
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 11, 26)
        backtest = YahooBacktest(BuyHold(), start=start_date, end=end_date)
        backtest.run()
