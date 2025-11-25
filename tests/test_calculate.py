from calculate import calculate_total

def test_calculate_no_discount():
    assert calculate_total(100, 2, 0) == 200

def test_calculate_with_discount():
    assert calculate_total(100, 2, 10) == 180

def test_calculate_zero_qty():
    assert calculate_total(100, 0, 10) == 0
