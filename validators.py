
def validate_symbol(symbol):
    """
    Validates the trading symbol.
    """
    if not symbol:
        return False, "Symbol cannot be empty."
    if not symbol.isalnum():
        return False, "Symbol must contain only letters and numbers."
    return True, symbol.upper()

def validate_side(side):
    """
    Validates the order side (BUY or SELL).
    """
    if not side:
        return False, "Side cannot be empty."
    side_upper = side.upper()
    if side_upper not in ["BUY", "SELL"]:
        return False, "Side must be 'BUY' or 'SELL'."
    return True, side_upper

def validate_quantity(quantity):
    """
    Validates the order quantity.
    """
    try:
        qty = float(quantity)
        if qty <= 0:
            return False, "Quantity must be greater than 0."
        return True, qty
    except ValueError:
        return False, "Quantity must be a valid number."

def validate_price(price):
    """
    Validates the order price.
    """
    try:
        p = float(price)
        if p <= 0:
            return False, "Price must be greater than 0."
        return True, p
    except ValueError:
        return False, "Price must be a valid number."
