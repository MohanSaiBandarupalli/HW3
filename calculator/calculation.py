"""
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
