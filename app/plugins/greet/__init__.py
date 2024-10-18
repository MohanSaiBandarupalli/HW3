import logging
from app.commands import Command

class GreetCommand(Command):
    def execute(self):
        logging.info("Executing GreetCommand")  # Log when the command is executed
        print("Hello, World!")
