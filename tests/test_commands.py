"""
Unit tests for command handling in the app module.
"""

from app import App
from app.commands import Command

# Mock command class for greet
class MockGreetCommand(Command):
    """A mock class for testing the greet command."""
    def execute(self):
        print("Hello, World!")

# Mock command class for goodbye
class MockGoodbyeCommand(Command):
    """A mock class for testing the goodbye command."""
    def execute(self):
        print("Goodbye")

def test_greet_command(capfd):
    """Test that the greet command prints 'Hello, World!'."""
    app = App()
    app.command_handler.register_command("greet", MockGreetCommand())  # Register the mock greet command
    app.command_handler.execute_command("greet")
    out, _ = capfd.readouterr()
    assert "Hello, World!" in out

def test_goodbye_command(capfd):
    """Test that the goodbye command prints 'Goodbye'."""
    app = App()
    app.command_handler.register_command("goodbye", MockGoodbyeCommand())  # Register the mock goodbye command
    app.command_handler.execute_command("goodbye")
    out, _ = capfd.readouterr()
    assert "Goodbye" in out
