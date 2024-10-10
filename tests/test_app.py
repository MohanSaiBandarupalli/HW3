"""
Test file for the App class and its functionality.
"""

import pytest
from app import App, AppExitException
from app.commands import Command


class GreetCommand(Command):
    """A simple greet command class."""
    def execute(self):
        print("Hello, World!")


def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App(max_loops=1)
    with pytest.raises(AppExitException):
        app.start()


def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App(max_loops=2)
    with pytest.raises(AppExitException):
        app.start()

    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out


def test_app_register_and_execute_valid_command(capfd, monkeypatch):
    """Test that a valid registered command is executed correctly."""
    app = App(max_loops=1)
    app.command_handler.register_command("greet", GreetCommand())
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(AppExitException):
        app.start()
    captured = capfd.readouterr()
    assert "Hello, World!" in captured.out


def test_app_max_loops(monkeypatch):
    """Test that the app exits after the specified number of loops."""
    app = App(max_loops=2)
    inputs = iter(['test', 'test', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(AppExitException):
        app.start()


def test_app_exit_on_keyboard_interrupt(monkeypatch):
    """Test that the app exits on keyboard interrupt."""
    app = App()

    def mock_input(_):
        raise KeyboardInterrupt

    monkeypatch.setattr('builtins.input', mock_input)

    with pytest.raises(KeyboardInterrupt):
        app.start()
