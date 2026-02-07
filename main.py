'''🔹 Q2: File-Based To-Do List
Task:
Create a to-do list that:
    adds tasks
    deletes tasks
    views tasks
    saves tasks to file
    loads tasks on start
Concepts: list, file I/O, loop '''
tasks = []
import os
if os.path.exists("to-do.txt"):
    with open("to-do.txt") as f:
        lines = f.readlines()
    for line in lines:
        task = line.strip()[3:]
        tasks.append(task)
def AddTask():
    task = input("Enter task: ")
    tasks.append(task)
    with open("to-do.txt","w") as f:
        count = 1
        for t in tasks:
            f.write(str(count)+". "+t+"\n")
            count+=1
    print("Task added successfully.")
    ShowMenu()

def ViewTasks():
    print("\n------ Tasks List ------")
    count = 1
    for t in tasks:
        print(count,"\b.",t)
        count+=1
    print("------------------------")
    # ShowMenu()
def DeleteTask():
    ViewTasks()
    num = int(input("Enter task number to delete: "))
    if num<1 or num>len(tasks):
        print("Invalid task number")
        return
    tasks.pop(num-1)
    with open("to-do.txt","w") as f:
        count = 1
        for t in tasks:
            f.write(str(count)+". "+t+"\n")
            count+=1
    print("Task deleted successfully.")
    ShowMenu()

def ShowMenu():
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("0. Exit")
    choice = int(input("Enter choise: "))
    if choice == 0:
        print("Program terminated.")
        return
    elif choice == 1:
        AddTask()
    elif choice == 2:
        ViewTasks()
        ShowMenu()
    elif choice == 3:
        DeleteTask()
    else:
        print("Choose between 0 to 2")
        ShowMenu()
# print("======= To-Do List App ========")
print("========================")
print("     To-Do List App")
print("========================")
ShowMenu()
