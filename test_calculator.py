from Calculator import square_root, factorial, natural_log, power

import pytest
import math

def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    with pytest.raises(ValueError):
        square_root(-1)  # Test for a negative number, should raise ValueError

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    with pytest.raises(ValueError):
        factorial(-1)  # Test for a negative number, should raise ValueError

def test_natural_log():
    assert natural_log(math.e) == 1
    assert natural_log(1) == 0
    with pytest.raises(ValueError):
        natural_log(0)  # Test for log(0), should raise ValueError

def test_power():
    assert power(2, 3) == 8
    assert power(2, -2) == 0.25
    assert power(2, 0) == 1
