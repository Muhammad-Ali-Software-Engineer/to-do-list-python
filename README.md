# File-Based To-Do List App 📝

A simple Python console application for managing tasks. This app allows you to:

- Add tasks
- View all tasks
- Delete tasks
- Automatically save tasks to a file (`to-do.txt`)
- Load tasks on program start

---

## Features

1. **Add Task**: Enter a task and it will be saved to your list.
2. **View Tasks**: See all your tasks with their numbers.
3. **Delete Task**: Remove a task by its number.
4. **Persistent Storage**: All tasks are saved in a text file, so they remain after closing the program.

---

## How It Works

- On start, the program checks if a `to-do.txt` file exists. If yes, it loads the tasks.
- When you add or delete tasks, the file updates automatically.
- Tasks are displayed with a number, making it easy to delete the correct one.

---

## Installation

1. Make sure you have **Python 3.x** installed.
2. Clone this repository:

```bash
git clone https://github.com/your-username/file-based-todo.git
```
3. Navigate to the project folder:
```
cd file-based-todo
```
4. Run the application:
```
Run the application:
```
## Usage
1. Launch the program.
2. Follow the menu to add, view, or delete tasks.
3. Tasks will be saved automatically in to-do.txt.
### Example:
```
========================
     To-Do List App
========================

1. Add task
2. View tasks
3. Delete task
0. Exit
Enter choice: 1
Enter task: Finish homework
Task added successfully.
```
