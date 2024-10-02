"""
This module provides the Calculator class for performing basic arithmetic operations.
"""

from decimal import Decimal
from typing import Callable
from .operations import add, subtract
class Calculator:
    """
    A class to perform basic arithmetic operations.
    """

    def __init__(self):
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
            raise ValueError("Cannot divide by zero")
        return a / b
