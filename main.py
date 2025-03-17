def main():

    print("Welcome to TaskTracker! type help to see menu")

    while True:

        command = input("Enter command: ").strip().lower()

        if command == "help":
            print("Command: \n")
            print("Help - Show this help menu")
            print("Greet - Say hello to the user")
            print("exit - Exit program")

        elif command == "Greet":
            name = input("Enter your name: ").strip()
            print(f"Hello {name}!")

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid command! Type help to see menu")
            
