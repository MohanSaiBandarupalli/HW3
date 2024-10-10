"""
Tests for the App class and command handling.
"""

import pytest
from app import App

def test_app_get_environment_variable():
    """Test retrieving environment variables from the App."""
    app = App()
    current_env = app.get_environment_variable('ENVIRONMENT')
    assert current_env == 'TESTING'

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit):
        app.start()

def test_app_start_unknown_command(monkeypatch, capfd):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):  # Expect SystemExit for 'exit'
        app.start()

    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_app_register_and_execute_valid_command(monkeypatch, capfd):
    """Test that a valid registered command is executed correctly."""
    app = App()
    app.command_handler.register_command("greet", lambda: print("Hello, World!"))
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "Hello, World!" in captured.out
