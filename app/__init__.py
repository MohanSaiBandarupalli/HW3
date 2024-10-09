class App:
    @staticmethod
    def start():
        """Starts the REPL loop to handle user commands."""
        print("Hello World. Type 'exit' to exit.")
        while True:
            command = input("Enter command: ")
            if command == 'exit':
                print("Exiting the app...")
                break
            else:
                App.handle_command(command)

    @staticmethod
    def handle_command(command: str):
        """Handles individual commands passed to the app."""
        parts = command.split()
        if len(parts) != 3:
            print(f"No such command: {command}")
            return
        a, operation, b = parts
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            print(f"Invalid number input: '{a}' or '{b}' is not a valid number.")
            return

        if operation == 'add':
            result = a + b
            print(f"The result of {a} add {b} is equal to {result}")
        elif operation == 'subtract':
            result = a - b
            print(f"The result of {a} subtract {b} is equal to {result}")
        elif operation == 'multiply':
            result = a * b
            print(f"The result of {a} multiply {b} is equal to {result}")
        elif operation == 'divide':
            if b == 0:
                print("Error: Division by zero.")
            else:
                result = a / b
                if result.is_integer():
                    result = int(result)
                print(f"The result of {a} divide {b} is equal to {result}")
        else:
            print(f"Unknown operation: {operation}")
