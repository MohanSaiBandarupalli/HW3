"""
<<<<<<< HEAD
This module provides the Calculator class for performing basic arithmetic operations.
=======
This module initializes the calculator package and exposes the necessary
classes and functions for performing arithmetic operations and managing
calculation history.
>>>>>>> Part-3
"""

from decimal import Decimal
from typing import Callable

<<<<<<< HEAD
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
=======
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide


class Calculator:
    """A simple calculator class to perform arithmetic operations."""

    @staticmethod
    def _perform_operation(
        a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]
    ) -> Decimal:
        """Perform the specified operation on two decimal numbers.

        Args:
            a (Decimal): The first operand.
            b (Decimal): The second operand.
            operation (Callable): The arithmetic operation to perform.

        Returns:
            Decimal: The result of the operation.
        """
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Add two numbers."""
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Subtract the second number from the first."""
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Multiply two numbers."""
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Divide the first number by the second."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Calculator._perform_operation(a, b, divide)
>>>>>>> Part-3
