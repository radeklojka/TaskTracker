#\tasktracker/>python main.py

def main():

    print("Welcome to TaskTracker! type help to see menu")

    while True:

        command = input("Enter command: ").strip().lower()

        if command == "help":
            print("Commands: \n")
            print("Help - Show this help menu")
            print("Greet - Say hello to the user")
            print("exit - Exit program")

        elif command == "greet":
            database = []
            name = str(input("Enter your name: ")).strip()
            database.append(name)
            print(f"Hello {name}!")
            print(database)

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid command! Type help to see menu")

if __name__ == "__main__":
    main()
            
