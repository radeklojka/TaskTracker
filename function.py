def add():
    ask = str(input("Add a task: ")).strip()
    database.append(task)
    print(database)

def show():
    print(database)

def delete():
    print(database)
    index = int(input("Which task do you wish to delete (type index of the task): "))
    database.pop(index)
    print(database)

def exit():
    print("Goodbye!")
