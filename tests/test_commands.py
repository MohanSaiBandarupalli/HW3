"""
Unit tests for command classes, including GreetCommand, GoodbyeCommand, and REPL command handling.
"""

from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand

def test_greet_command(capfd):
    """Test the GreetCommand prints 'Hello, World!'."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Hello, World!\n"

def test_goodbye_command(capfd):
    """Test the GoodbyeCommand prints 'Goodbye'."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Goodbye\n"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    App.start()
    out, _ = capfd.readouterr()
    assert "Hello, World!" in out
    assert "Exiting the app..." in out

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    App.start()
    out, _ = capfd.readouterr()
    assert "Displaying menu" in out
    assert "Exiting the app..." in out
