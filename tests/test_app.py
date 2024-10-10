"""
Unit tests for the App class in the app module.
"""

from app import App
from app.commands import Command

# A mock command class that simulates an add operation
class MockAddCommand(Command):
    """A mock class for testing the add command."""
    def execute(self):
        print("Result: 8")

def test_handle_add_command(capfd, monkeypatch):
    """Test handling the 'add' operation."""
    app = App(max_loops=1)  # Limit the number of loops for testing
    app.command_handler.register_command("add", MockAddCommand())  # Register the mock command

    # Mock input to simulate the 'add' command
    monkeypatch.setattr('builtins.input', lambda _: 'add')
    app.start()

    out, _ = capfd.readouterr()
    assert "Result: 8" in out
