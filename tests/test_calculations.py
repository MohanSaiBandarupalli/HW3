"""
My Calculator Test
"""

from decimal import Decimal
import pytest
from calculator.operations import add, multiply, subtract, divide
from ..calculator.operations import add, multiply, subtract, divide


def test_addition():
    """Test that the addition function works."""
    assert add(Decimal(2), Decimal(2)) == Decimal(4)

def test_subtraction():
    """Test that the subtraction function works."""
    assert subtract(Decimal(2), Decimal(2)) == Decimal(0)

def test_multiplication():
    """Test that the multiplication function works."""
    assert multiply(Decimal(2), Decimal(2)) == Decimal(4)

def test_division():
    """Test that the division function works."""
    assert divide(Decimal(2), Decimal(2)) == Decimal(1)

def test_division_by_zero():
    """Test that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(Decimal(2), Decimal(0))
