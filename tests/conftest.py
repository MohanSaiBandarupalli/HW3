import pytest
from faker import Faker
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal

fake = Faker()

@pytest.fixture(scope='session')
def setup_calculation_history():
    """Setup for generating test data."""
    history = []
    for _ in range(100):  # Change this to the desired number of records
        a = fake.random_number(digits=2)
        b = fake.random_number(digits=2)
        operation = fake.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
        expected = {
            'add': a + b,
            'subtract': a - b,
            'multiply': a * b,
            'divide': a / b if b != 0 else 'Cannot divide by zero'
        }[operation]
        history.append((Decimal(a), Decimal(b), operation, expected))
    return history

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, help="Number of records to generate")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    num_records = config.getoption("num_records")
    if num_records:
        records = setup_calculation_history()
        for record in records:
            yield record  # yields the test data for each test case
