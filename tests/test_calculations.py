"""
<<<<<<< HEAD
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
=======
This module contains unit tests for the calculator functionality.
"""

from decimal import Decimal  # Standard library imports first
import pytest  # Third-party imports after

from calculator.calculations import Calculations  # Local imports after third-party imports
from calculator.calculation import Calculation
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Calculations.clear_history()  # Clear existing history for a clean state
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

# pylint: disable=unused-argument, redefined-outer-name
def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, \
        "Failed to add the calculation to the history"

# pylint: disable=unused-argument, redefined-outer-name
def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"

# pylint: disable=unused-argument, redefined-outer-name
def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

# pylint: disable=unused-argument, redefined-outer-name
def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest()
    assert latest is not None, "No calculations found in the history"
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), \
        "Did not get the correct latest calculation"

# pylint: disable=unused-argument, redefined-outer-name
def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, \
        "Did not find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, \
        "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, \
        "Expected None for latest calculation with empty history"
>>>>>>> Part-3
