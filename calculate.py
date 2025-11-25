def calculate_total(price, qty, discount):
    subtotal = price * qty
    return subtotal - (subtotal * discount / 100)
