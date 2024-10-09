"""
This module provides pytest fixtures and setup for generating test data for calculator operations.
"""

from decimal import Decimal
import pytest
from faker import Faker

# Initialize the Faker instance
fake = Faker()

@pytest.fixture(scope='session')
def setup_calculation_history(request):
    """
    Fixture that sets up a history of calculations with random test data.
    """
    history = []
    num_records = int(request.config.getoption("--num_records"))  # Get the number of records from command line
    for _ in range(num_records):
        a = fake.random_number(digits=2)
        b = fake.random_number(digits=2)
        operation = fake.random_element(elements=('add', 'subtract', 'multiply', 'divide'))

        # Determine the expected result based on the operation
        expected = {
            'add': a + b,
            'subtract': a - b,
            'multiply': a * b,
            'divide': a / b if b != 0 else 'Cannot divide by zero'
        }[operation]

        # Append a tuple (operand1, operand2, operation, expected result) to the history
        history.append((Decimal(a), Decimal(b), operation, expected))

    return history

def pytest_addoption(parser):
    """
    Adds a command line option to specify the number of test records to generate.
    """
    parser.addoption(
        "--num_records",
        action="store",
        default=10,
        help="Number of test records to generate"
    )

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Configure pytest to handle the --num_records option for generating test data.
    """
    num_records = config.getoption("num_records")
    if num_records:
        records = setup_calculation_history(config)
        yield from records  # Use 'yield from' to yield records directly
