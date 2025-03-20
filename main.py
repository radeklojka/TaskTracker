
#python3 main.py           

import function

def main():
    database = []
    print("Welcome to TaskTracker! type help to see menu")

    while True:

        command = input("Enter command (For options type 'help'): ").strip().lower()

        if command == "help":
            print("Commands: \n")
            print("Help - Show this help menu")
            print("Add - Add a task")
            print("Show - Shows list")
            print("Delete - Delete a task")
            print("Exit - Exit program")

        elif command == "add":
           function.add()

        elif command == "show":
            function.show()
        
        elif command == "delete":
            function.delete()

        elif command == "exit":
            function.exit()

        else:
            print("Invalid command! Type help to see menu")

if __name__ == "__main__":
    main()
            
