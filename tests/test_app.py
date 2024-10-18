"""
Test suite for the App class and its command handling functionality.
"""

import pytest
from app import App

def test_app_get_environment_variable():
    """
    Test retrieving the current environment variable from the app.
    """
    app = App()
    current_env = app.get_environment_variable('ENVIRONMENT')
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_start_exit_command(capfd, monkeypatch):
    """
    Test that the REPL exits correctly on 'exit' command.
    """
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """
    Test how the REPL handles an unknown command before exiting.
    """
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out
