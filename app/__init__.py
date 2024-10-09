# app/__init__.py
from decimal import Decimal, InvalidOperation

class App:
    @staticmethod
    def start() -> None:
        print("Hello World. Type 'exit' to exit.")
        
        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            else:
                App.handle_command(user_input)

    @staticmethod
    def handle_command(command: str) -> None:
        parts = command.split()
        if len(parts) == 3 and parts[1] in ['add', 'subtract', 'multiply', 'divide']:
            try:
                a = Decimal(parts[0])
                b = Decimal(parts[2])
                operation = parts[1]

                # Perform the operation and prepare the output message
                if operation == 'add':
                    result = a + b
                    print(f"The result of {command} is equal to {result}")
                elif operation == 'subtract':
                    result = a - b
                    print(f"The result of {command} is equal to {result}")
                elif operation == 'multiply':
                    result = a * b
                    print(f"The result of {command} is equal to {result}")
                elif operation == 'divide':
                    if b == 0:
                        print("Error: Division by zero.")
                        return
                    result = a / b
                    print(f"The result of {command} is equal to {result}")

            except InvalidOperation:
                print(f"Invalid number input: '{parts[0]}' or '{parts[2]}' is not a valid number.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Unknown command. Type 'exit' to exit.")
