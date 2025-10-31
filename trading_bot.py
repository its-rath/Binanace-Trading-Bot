
import logging
from binance import Client
from binance.exceptions import BinanceAPIException

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.logger = logging.getLogger(__name__)

    def place_market_order(self, symbol, side, quantity):
        try:
            self.logger.info(f"Placing market order: {side} {quantity} {symbol}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            self.logger.info(f"Market order placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            self.logger.info(f"Placing limit order: {side} {quantity} {symbol} @ {price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price
            )
            self.logger.info(f"Limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Error placing limit order: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            self.logger.info(f"Placing stop limit order: {side} {quantity} {symbol} @ {price}, stop_price: {stop_price}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='STOP',
                timeInForce='GTC',
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )
            self.logger.info(f"Stop limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Error placing stop limit order: {e}")
            return None
