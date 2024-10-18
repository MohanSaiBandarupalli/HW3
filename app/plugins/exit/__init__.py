import logging
import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self):
        logging.info("Executing ExitCommand: Exiting the application.")  # Log the exit action
        print("Exiting the application...")  # Print an exit message to the console
        sys.exit(0)  # Exit with status code 0 (indicating success)
