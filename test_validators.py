
import unittest
from validators import validate_symbol, validate_side, validate_quantity, validate_price

class TestValidators(unittest.TestCase):
    def test_symbol(self):
        self.assertEqual(validate_symbol("BTCUSDT"), (True, "BTCUSDT"))
        self.assertEqual(validate_symbol("btcusdt"), (True, "BTCUSDT"))
        self.assertEqual(validate_symbol(""), (False, "Symbol cannot be empty."))
        self.assertEqual(validate_symbol("BTC-USDT"), (False, "Symbol must contain only letters and numbers."))

    def test_side(self):
        self.assertEqual(validate_side("BUY"), (True, "BUY"))
        self.assertEqual(validate_side("sell"), (True, "SELL"))
        self.assertEqual(validate_side("HOLD"), (False, "Side must be 'BUY' or 'SELL'."))

    def test_quantity(self):
        self.assertEqual(validate_quantity("10.5"), (True, 10.5))
        self.assertEqual(validate_quantity("0"), (False, "Quantity must be greater than 0."))
        self.assertEqual(validate_quantity("-5"), (False, "Quantity must be greater than 0."))
        self.assertEqual(validate_quantity("abc"), (False, "Quantity must be a valid number."))

    def test_price(self):
        self.assertEqual(validate_price("100"), (True, 100.0))
        self.assertEqual(validate_price("-10"), (False, "Price must be greater than 0."))

if __name__ == '__main__':
    unittest.main()
