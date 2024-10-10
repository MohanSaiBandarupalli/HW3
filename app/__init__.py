import os
import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from dotenv import load_dotenv

class App:
    def __init__(self):  # Constructor
        load_dotenv()
        self.settings = {}  # Initialize settings as an empty dictionary
        # Load all environment variables into settings
        for key, value in os.environ.items():
            self.settings[key] = value
        # Default to 'PRODUCTION' if 'ENVIRONMENT' not set
        self.settings.setdefault('ENVIRONMENT', 'TESTING')        
        self.command_handler = CommandHandler()

    def get_environment_variable(self, envvar: str = 'ENVIRONMENT'):  # Updated to snake_case
        return self.settings.get(envvar, 'Not Set')  # Added default return for safety
    
    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):  # Assuming Command as the base class
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        """Start the application and handle commands in REPL format."""
        self.load_plugins()
        print("Application started. Type 'exit' to exit.")
        while True:
            command_input = input(">>> ").strip()
            if command_input.lower() == 'exit':
                print("Exiting the app...")
                raise SystemExit  # Exit cleanly
            else:
                self.command_handler.execute_command(command_input)
