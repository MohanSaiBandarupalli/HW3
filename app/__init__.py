from app.commands import CommandHandler

class App:
    def __init__(self, max_loops=None):
        self.command_handler = CommandHandler()
        self.max_loops = max_loops  # Limit the number of input loops (for testing)

    def start(self):
        print("Type 'exit' to exit.")
        loops = 0
        while True:
            command = input(">>> ").strip()
            if command == 'exit':
                print("Exiting the app...")
                break
            else:
                self.command_handler.execute_command(command)

            # Break after max_loops during testing (if max_loops is set)
            if self.max_loops is not None:
                loops += 1
                if loops >= self.max_loops:
                    break
