"""
This module defines arithmetic operations for the calculator.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Divide the first number by the second.

    Raises:
        ValueError: If the second number (b) is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
