"""
This module provides the Calculator class for performing basic arithmetic operations.
"""

from decimal import Decimal
from typing import Callable

class Calculator:
    """
    A class to perform basic arithmetic operations including addition,
    subtraction, multiplication, and division.
    """

    def __init__(self):
        """Initialize the Calculator class."""
        pass

    def add(self, a: Decimal, b: Decimal) -> Decimal:
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a: Decimal, b: Decimal) -> Decimal:
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a: Decimal, b: Decimal) -> Decimal:
        """Return the product of a and b."""
        return a * b

    def divide(self, a: Decimal, b: Decimal) -> Decimal:
        """Return the quotient of a and b. Raise ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero; the divisor must not be zero.")
        return a / b
