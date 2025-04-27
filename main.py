"""
CLI-BASED TASK-MANAGER

PROGRAM DESCRIPTION: This is a CLI-based task manager that will ADD, UPDATE, TRACK and
DELETE tasks and then store them in a JSON file.

DATE STARTED: 04 APR 2025
DATE FINISHED: -TBA-
"""

import os
import datetime as dt

def main_menu() -> str:
    # displays the main menu of choices
    MENU_PADDING: int = 5
    WIDTH: int = 100
    LOCATION: int = 1

    header(WIDTH, LOCATION)
    print("")
    print(f" " * MENU_PADDING + "MAIN MENU OPTIONS")
    print("")
    print(f" " * MENU_PADDING + "[A] : ADD TASK")
    print(f" " * MENU_PADDING + "[B] : UPDATE TASK")
    print(f" " * MENU_PADDING + "[C] : DELETE TASK")
    print(f" " * MENU_PADDING + "[D] : DISPLAY ALL TASKS")
    print(f" " * MENU_PADDING + "[E] : FLITER BY STATUS")
    print(f" " * MENU_PADDING + "[F] : EXIT")
    print("")

    print("")
    print(f"." * WIDTH)
    print("")
    choice: str = input(f" " * MENU_PADDING + "YOUR CHOICE -> ")
    print("")

    choice = choice.upper()
    return choice

def generate_task_id() -> int:
    # generates and a new task id
    id = 1
    
    return id

def task_initializer() -> dict:
    # initializes the dictionary for the task
    task = {
        'description': ' ',
        'status': ' ',
        'created_at': dt.datetime.now(),
        'updated_at': 'N/A'
    }

    return task

def task_status_is(choice: str) -> str:
    # gets the task status depending on the user choice
    match choice:
        case 'A':
            status = "TODO"
        case 'B':
            status = 'IN PROGRESS'
        case 'C':
            status = 'DONE'

    return status

def input_task(task_records):
    # ask the user for the task and task status and stores it in a dictionary
    os.system('cls || clear')
    records = task_records
    WIDTH: int = 100
    LOCATION: int = 2
    header(WIDTH, LOCATION)

    # generate the task_id
    task_id = generate_task_id()

    print(f"TASK ID: {task_id}")
    # initialize a temporary dictionary
    task = task_initializer()

    # ask for description
    print("ENTER TASK DESCRIPTION")
    task_description_input: str = input("-> ")

    print("")
    print("ENTER TASK STATUS")
    print("[A]: TODO")
    print("[B]: IN PROGRESS")
    print("[C]: DONE")
    
    print("")
    print("ENTER CHOICE")
    task_status_user_choice: str = input("-> ")
    task_status_user_choice = task_status_user_choice.upper()
    task_status = task_status_is(task_status_user_choice)

    print("")
    is_user_continue = input("Are you sure you want to continue? (Y/N): ")
    is_user_continue = is_user_continue.upper()
    
    match is_user_continue:
        case 'Y':
            task.update({
                'description': task_description_input,
                'status': task_status,
                })
            records.update({task_id:task})
            return records
        case 'N':
            return records
        
def validate_choice(user_choice: str, task_records: dict): 
    # gets the user choice and sends them to the appropriate method
    match user_choice:
        case 'A':
                task_records = input_task(task_records)
        case 'B':
            pass
        case 'C':
            pass
        case 'D':
            pass
        case 'E':
            pass
        case 'F':
            exit()
        case _:
            error_validation(error_code=100)

    return task_records

def error_validation(error_code: int):
    # gets the error code and displays the appropriate error message
    match error_code:
        case 100:
            print(f"ERROR {error_code}: Invalid Choice! Choose between A - F")
            input("Press ANY KEY to continue...")
            

def header(WIDTH: int, LOCATION_CODE: int) -> None:
    # displays the appropriate location for header based on the location code
    match LOCATION_CODE: 
        case 1:
            LOCATION = "MAIN MENU"
        case 2: 
            LOCATION = "UPDATE TASK"
        case 3: 
            LOCATION = "DELETE TASK"
        case 4:
            LOCATION = "DISPLAY ALL TASKS"
        case 5:
            LOCATION = "FILTER: TASKS DONE"
        case 6: 
            LOCATION = "FILTER: TASKS NOT DONE"
        case 7:
            LOCATION = "FILTER: TASKS IN PROGRESS"

    print(f"." * WIDTH)
    print(f" " * 30 + "TASKMAN - THE CLI-BASED TASK MANAGER")
    print(f" " * 37 + "YOU ARE IN: ", LOCATION)
    print(f"." * WIDTH)

def main():
    task_records = {}

    user_choice = main_menu()
    task_records = validate_choice(user_choice, task_records)
    print(task_records)

if __name__ == '__main__':
    main()