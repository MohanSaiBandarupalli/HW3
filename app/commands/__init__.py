from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class GreetCommand(Command):
    def execute(self):
        print("Hello, World!")

class MenuCommand(Command):
    def execute(self):
        print("Displaying menu")

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """EAFP - Try to execute the command, if it doesn't exist handle it."""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
