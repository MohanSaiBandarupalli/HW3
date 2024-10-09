"""
This module contains tests for the App class.
"""

from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    App.start()
    out, _ = capfd.readouterr()
    assert "Hello World. Type 'exit' to exit." in out
    assert "Exiting the app..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Hello World. Type 'exit' to exit." in out
    assert "Invalid command format." in out
    assert "Exiting the app..." in out

def test_handle_add_command(capfd):
    """Test handling the 'add' operation."""
    App.handle_command("5 add 3")
    out, _ = capfd.readouterr()
    assert "The result of 5 add 3 is equal to 8" in out

def test_handle_subtract_command(capfd):
    """Test handling the 'subtract' operation."""
    App.handle_command("10 subtract 4")
    out, _ = capfd.readouterr()
    assert "The result of 10 subtract 4 is equal to 6" in out

def test_handle_multiply_command(capfd):
    """Test handling the 'multiply' operation."""
    App.handle_command("7 multiply 6")
    out, _ = capfd.readouterr()
    assert "The result of 7 multiply 6 is equal to 42" in out

def test_handle_divide_command(capfd):
    """Test handling the 'divide' operation."""
    App.handle_command("20 divide 4")
    out, _ = capfd.readouterr()
    assert "The result of 20 divide 4 is equal to 5" in out

def test_handle_divide_by_zero(capfd):
    """Test handling division by zero."""
    App.handle_command("10 divide 0")
    out, _ = capfd.readouterr()
    assert "Error: Division by zero." in out

def test_invalid_number_input(capfd):
    """Test handling invalid number input."""
    App.handle_command("a add 3")
    out, _ = capfd.readouterr()
    assert "Invalid number input: 'a' or '3' is not a valid number." in out

def test_unknown_operation(capfd):
    """Test handling an unknown operation."""
    App.handle_command("5 unknown 3")
    out, _ = capfd.readouterr()
    assert "Unknown command. Type 'exit' to exit." in out
