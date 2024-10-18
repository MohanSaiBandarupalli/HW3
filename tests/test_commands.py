"""
Tests for command handling in the REPL.
"""

import pytest
from app import App

def test_george_command(monkeypatch, capfd):
    """Test that the REPL correctly handles the 'george' command."""
    inputs = iter(['george', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.command_handler.register_command("george", lambda: print("Hello, George!"))
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "Hello George" in captured.out

def test_greet_command(monkeypatch, capfd):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.command_handler.register_command("greet", lambda: print("Hello, World!"))
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "Hello, World!" in captured.out

def test_menu_command(monkeypatch, capfd):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.command_handler.register_command("menu", lambda: print("Menu"))
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "Menu" in captured.out

def test_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()
        