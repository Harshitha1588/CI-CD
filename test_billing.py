import pytest
from billing import calculate_total

def test_calculate_total_normal():
    assert calculate_total(100, 2, 10) == 180.0

def test_without_discount():
    assert calculate_total(50, 4, 0) == 200.0

def test_with_high_discount():
    assert calculate_total(200, 1, 50) == 100.0

def test_zero_quantity():
    assert calculate_total(100, 0, 10) == 0.0

def test_negative_price_error():
    with pytest.raises(ValueError):
        calculate_total(-10, 5, 10)

def test_negative_qty_error():
    with pytest.raises(ValueError):
        calculate_total(100, -5, 10)

def test_negative_discount_error():
    with pytest.raises(ValueError):
        calculate_total(100, 5, -20)
