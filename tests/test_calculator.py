from app import calculator

def test_add():
    assert calculator.add(3, 2) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 5) == -5

def test_multiply():
    assert calculator.multiply(4, 3) == 12
    assert calculator.multiply(-1, 5) == -5

def test_divide():
    assert calculator.divide(10, 2) == 5
    try:
        calculator.divide(5, 0)
        assert False  # Should not reach here
    except ValueError:
        assert True
