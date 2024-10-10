"""
Test file for command handling in the app.
"""

import pytest
from app import App, AppExitException
from app.commands import Command

class GreetCommand(Command):
    """A simple greet command class."""
    def execute(self):
        print("Hello, World!")

class MenuCommand(Command):
    """A simple menu command class."""
    def execute(self):
        print("Displaying menu")

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.command_handler.register_command("greet", GreetCommand())

    with pytest.raises(AppExitException):
        app.start()

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.command_handler.register_command("menu", MenuCommand())

    with pytest.raises(AppExitException):
        app.start()
