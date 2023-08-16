# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# Change Log:
# RRoot,1.1.2030, Created started script
# Zeynep,8/14/23, Modified code to complete assignment 06
#        8/15/23, Finalized code
# ---------------------------------------------------------------------------- #

# Data Layer ---------------------------------------------------------------------- #
# Declare variables and constants



file_name_str = "ToDoList.txt"  # The name of the data file
file_obj = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing Layer --------------------------------------------------------------- #
# Functions that process the data

class Process:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want to add more data to:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        list_of_rows.append(row)
        print("Task added to your to do list")
        return list_of_rows

    @staticmethod
    def remove_data_from_list(priority, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param priority: (string) with priority of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        for row in list_of_rows:
            if row['Priority'] == priority:
                task = row['Task']
                list_of_rows.remove(row)
                print(f"Task {task} with priority {priority} has been removed.")
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        print("Data Saved!")
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #
# Functions that prompts user for input or prints results out

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new task
        3) Remove an existing task
        4) Save data to file        
        5) Exit program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        while choice not in ('1', '2', '3', '4', '5'):
            choice = str(input("Please enter a valid option [1-5]")).strip()
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        new_task = str(input("Please enter task: ")).strip()
        new_task_priority = str(input("What is the priority? - ")).strip()
        while any(task['Priority'] == new_task_priority for task in lstTable):
            new_task_priority = str(input(f"Please set a different priority or first delete the task with the priority of {new_task_priority}\n")).strip()
        return new_task, new_task_priority


    @staticmethod
    def input_task_to_remove():
        """  Gets the priority to be removed from the list

        :return: (string) with priority
        """
        priority2Bremoved = str(input("Enter the priority of the task to remove: ")).strip()
        while not any(priority['Priority'] == priority2Bremoved for priority in lstTable):
            priority2Bremoved = str(input("The priority you entered is not on the list. Please enter a valid priority \n")).strip()
        return priority2Bremoved

# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
Process.read_data_from_file(file_name=file_name_str, list_of_rows=lstTable)  # read file data

while (True):
    # Step 2 - Display a menu of choices to the user
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 3 Show current data
    if choice_str.strip() == '1':  # Show current data in the list/table
        IO.output_current_tasks_in_list(list_of_rows=lstTable)

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '2':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        lstTable = Process.add_data_to_list(task=task, priority=priority, list_of_rows=lstTable)
        continue  # to show the menu

    elif choice_str == '3':  # Remove an existing Task
        priority = IO.input_task_to_remove()
        lstTable = Process.remove_data_from_list(priority=priority, list_of_rows=lstTable)
        continue  # to show the menu

    elif choice_str == '4':  # Save Data to File
        lstTable = Process .write_data_to_file(file_name=file_name_str, list_of_rows=lstTable)
        continue  # to show the menu

    elif choice_str == '5':  # Exit Program
        print("Good luck with those tasks. Goodbye!")
        break  # by exiting loop

