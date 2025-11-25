def calculate_total(price, qty, discount):
    """
    price: price of each item
    qty: quantity of items
    discount: discount percentage
    """
    if price < 0 or qty < 0 or discount < 0:
        raise ValueError("Negative values are not allowed")

    subtotal = price * qty
    discount_amount = subtotal * (discount / 100)
    total = subtotal - discount_amount

    return round(total, 2)
