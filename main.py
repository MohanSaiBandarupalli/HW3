import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        # Convert inputs to Decimal
        a_decimal, b_decimal = map(Decimal, [a, b])
        
        # Fetch the operation from the dictionary
        operation = operation_mappings.get(operation_name)

        if operation:
            # Perform the calculation and print the result
            result = operation(a_decimal, b_decimal)
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            print(f"Unknown operation: {operation_name}")
    
    # Handle invalid number input
    except InvalidOperation:
        print(f"Invalid number input: '{a}' or '{b}' is not a valid number.")
    
    # Handle division by zero
    except ZeroDivisionError:
        print("Error: Division by zero.")
    
    # Catch-all for other unexpected exceptions
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    # Extract command-line arguments
    _, a, b, operation = sys.argv

    # Call the function to perform the calculation and print the result
    calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()
