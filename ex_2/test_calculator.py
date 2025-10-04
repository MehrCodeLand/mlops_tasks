# ex_2/test_calculator.py
"""Pytest tests for calculator module"""

import pytest
from calculator import add, subtract, multiply, divide, power


class TestCalculator:
    """Test cases for calculator functions"""
    
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(100, 200) == 300
    
    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(10, 10) == 0
    
    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6
        assert multiply(0, 100) == 0
    
    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5
        assert divide(0, 5) == 0
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
    
    def test_power(self):
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 0) == 1


# Parametrized tests - testing multiple inputs at once
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (10, 20, 30),
    (-5, 5, 0),
    (0, 0, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected