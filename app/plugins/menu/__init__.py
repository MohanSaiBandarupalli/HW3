import logging
from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        logging.info("Executing MenuCommand")  # Log when the command is executed
        print("Menu")
