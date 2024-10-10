"""
Unit tests for the App class and its command handling.
"""

import pytest
from app import App
from app.commands import Command

# Define a simple AddCommand class for testing
class AddCommand(Command):
    """A command that adds two numbers."""
    def execute(self):
        print("Result: 8")

def test_handle_add_command(capfd, monkeypatch):
    """Test handling the 'add' operation."""
    app = App(max_loops=1)  # Limit the number of loops for testing
    app.command_handler.register_command("add", AddCommand())  # Register AddCommand
    monkeypatch.setattr('builtins.input', lambda _: 'add')
    with pytest.raises(SystemExit):  # Expect the system to exit cleanly after max_loops
        app.start()

    # Capture the output and check
    captured = capfd.readouterr()
    assert "Result: 8" in captured.out

def test_app_get_environment_variable():
    """Test environment variable retrieval."""
    app = App()
    current_env = app.get_environment_variable('ENVIRONMENT')
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test handling an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "No such command" in captured.out
