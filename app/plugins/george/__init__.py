import logging
from app.commands import Command

class GeorgeCommand(Command):
    def execute(self, context=None):
        logging.info("Executing GeorgeCommand")
        print("Hello George")  
