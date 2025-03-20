def add(database):
    task = str(input("Add a task: ")).strip()
    database.append(task)
    print(database)

def show(database):
    print(database)

def delete(database):
    print(database)
    index = int(input("Which task do you wish to delete (type index of the task): "))
    if 0 <= index < len(database):
        database.pop(index)
        print("Task at index {index} is deleted")
    else:
        print(database)

def exit():
    print("Goodbye!")
