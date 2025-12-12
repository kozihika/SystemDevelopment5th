"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


# ---- Extra divide tests (for mutation testing) ----
def test_divide_returns_float():
    calc = Calculator()
    assert calc.divide(5, 2) == 2.5


def test_divide_zero_numerator():
    calc = Calculator()
    assert calc.divide(0, 5) == 0


def test_divide_negative_numbers():
    calc = Calculator()
    assert calc.divide(-6, 3) == -2


def test_divide_by_one():
    calc = Calculator()
    assert calc.divide(7, 1) == 7


# ---- Original tests ----
class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        calc = Calculator()
        assert calc.add(5, 3) == 8

    def test_add_negative_numbers(self):
        calc = Calculator()
        assert calc.add(-5, -3) == -8

    def test_add_positive_and_negative(self):
        calc = Calculator()
        assert calc.add(5, -3) == 2

    def test_add_negative_and_positive(self):
        calc = Calculator()
        assert calc.add(-5, 3) == -2

    def test_add_positive_with_zero(self):
        calc = Calculator()
        assert calc.add(5, 0) == 5

    def test_add_zero_with_positive(self):
        calc = Calculator()
        assert calc.add(0, 5) == 5

    def test_add_floats(self):
        calc = Calculator()
        assert calc.add(2.5, 3.7) == pytest.approx(6.2)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        calc = Calculator()
        assert calc.subtract(5, 3) == 2


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        calc = Calculator()
        assert calc.multiply(5, 3) == 15


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        calc = Calculator()
        assert calc.divide(6, 3) == 2

