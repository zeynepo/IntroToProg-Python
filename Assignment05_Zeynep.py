# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# RRoot,1.1.2030,Created started script
# Zeynep,8/6/23, Added code to complete assignment 5
#       - added element strFile because that's how we were doing all the exercises
#       - took out element strMenu and strData because I felt it was unnecessary
#       - added element c to be able to assign Priority and count the number of tasks
#
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None
lstRow = []
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user

c = 0
lstTable = []  # A list that acts as a 'table' of rows
objFile = open(strFile, "r")
for row in objFile:
    tasks = row.strip().split("\n")  # Split the line into tasks
    for task in tasks:
        dicRow = {"Priority": c + 1, "Task": task}
        lstTable.append(dicRow)
        c += 1

while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        c = len(lstTable)
        print(f"Your {c} tasks to do are:")
        for task in lstTable:
            print(f"Priority {task['Priority']} Task: {task['Task']}")
        continue

    # Step 4 - Add a new item to the Table
    elif (strChoice.strip() == '2'):
        new_task = input("Please enter task: ")
        new_task_priority = len(lstTable) + 1
        dicRow = {"Priority": new_task_priority, "Task": new_task}
        lstTable.append(dicRow)
        print("Task added to your to do list")
        continue

    # Step 5 - Remove an item from the Table
    elif (strChoice.strip() == '3'):
        priority2remove = int(input("Enter the priority of the task to remove: "))
        task2remove = None
        for task in lstTable:
            if task['Priority'] == priority2remove:
                task2remove = task
                lstTable.remove(task)
                print(f"Task with Priority {priority2remove} has been removed.")
                break
        if task2remove:
            for task in lstTable:
                if task['Priority'] > priority2remove:
                    task['Priority'] -= 1

        else:
            print(f"No task found with priority {priority2remove}.")

        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for task in lstTable:
            objFile.write(f"{task['Task']}\n")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Good luck with those tasks!")
        break  # and Exit the program



