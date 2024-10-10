import os
from app.commands import CommandHandler

class AppExitException(Exception):
    """Custom exception to indicate that the app should exit."""
    pass

class App:
    def __init__(self, max_loops=None):
        self.command_handler = CommandHandler()
        self.max_loops = max_loops  # Limit the number of loops for testing

    def start(self):
        print("Application started. Type 'exit' to exit.")
        loops = 0
        while True:
            cmd_input = input(">>> ").strip()
            if cmd_input.lower() == 'exit':
                print("Exiting the app...")
                raise AppExitException  # Custom exception for clean exit
            else:
                try:
                    self.command_handler.execute_command(cmd_input)
                except KeyError:
                    print(f"No such command: {cmd_input}")

            # Break after max_loops during testing (if max_loops is set)
            if self.max_loops is not None:
                loops += 1
                if loops >= self.max_loops:
                    raise AppExitException
