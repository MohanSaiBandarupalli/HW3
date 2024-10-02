"""
<<<<<<< HEAD
Module for the Calculation class.
"""

class Calculation:
    """Class to perform operations on two numbers."""

    def __init__(self, a, b, operation):
        """Initialize with two numbers and an operation."""
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation function

    def get_result(self):
        """Return the result of the operation."""
        return self.operation(self.a, self.b)

    def perform_operation(self):
        """Perform and return the operation result."""
        return self.get_result()
=======
This module defines the Calculation class which performs arithmetic operations.
"""

from decimal import Decimal
from typing import Callable


class Calculation:
    """Represents a single arithmetic operation."""

    def __init__(
        self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]
    ):
        """Initialize with two numbers and an operation."""
        self.a = a
        self.b = b
        self.operation = operation

    @classmethod
    def create(
        cls, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]
    ) -> "Calculation":
        """Factory method to create a Calculation object."""
        return cls(a, b, operation)

    def perform(self) -> Decimal:
        """Return the result of the operation."""
        return self.operation(self.a, self.b)

    def __repr__(self):
        """Return a string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
>>>>>>> Part-3
