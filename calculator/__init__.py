"""
Calculator class for basic operations.
"""

from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    """A simple calculator class."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        calculation = Calculation(a, b, add)
        return calculation.get_result()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract the second number from the first."""
        calculation = Calculation(a, b, subtract)
        return calculation.get_result()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        calculation = Calculation(a, b, multiply)
        return calculation.get_result()

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide the first number by the second."""
        calculation = Calculation(a, b, divide)
        return calculation.get_result()
