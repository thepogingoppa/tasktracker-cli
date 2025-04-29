"""
CLI-BASED TASK-MANAGER

PROGRAM DESCRIPTION: This is a CLI-based task manager that will ADD, UPDATE, TRACK and
DELETE tasks and then store them in a JSON file.

DATE STARTED: 04 APR 2025
DATE FINISHED: -TBA-
"""

import os
import datetime as dt
import json

WIDTH: int = 150

def main_menu() -> str:
    # displays the main menu of choices
    MENU_PADDING: int = 5
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

def update_task(task_records):
    LOCATION: int = 2
    system_clear()
    header(WIDTH, LOCATION)
    table_header()
    looping_through(task_records)

    choice = (input("\nEnter the ID number of the record you wish to edit: "))
    for task in task_records.keys():
        id = task
        if choice == id:
            edit_choice(task_records, id)
            break

def edit_choice(task_records, id):
    print(f"\nEDITING THE FOLLOWING RECORD")
    print(f"\n'{id}: {task_records[id]['description'] + ", " + task_records[id]['status']}'\n")
    print("[1]: DESCRIPTION: ")
    print("[2]: TASK STATUS: ")

    edit_choice = int(input("\nChoose a record to edit: "))
    match edit_choice:
        case 1:
            print("\nENTER NEW DESCRIPTION")
            new_description = input("-> ")
            task_records[id]['description'] = new_description
        case 2: 
            new_status = input_status()
            task_records[id]['status'] = new_status

    sure_choice = input("Are you sure you want to edit records? (Y/N): ")
    sure_choice = sure_choice.upper()

    match sure_choice:
        case 'N':
            return
        case 'Y':
            date_today = dt.datetime.now()
            date_today = date_today.strftime("%d %b %Y (%I:%M %p)")
            task_records[id]['updated_at'] = date_today
            write_to_file(task_records)
            return

def generate_task_id() -> int:
    # generates and a new task id
    
    if isFileExists() == True:
        with open('task_records.json') as f:
            tasks = json.load(f)
            
        for task in tasks:
            keys = list(tasks.keys())

        id = int(keys[len(keys) - 1]) + 1
    else:
        id = 1
    
    return id

def isFileExists() -> bool:
    file_path = "task_records.json"

    if os.path.exists(file_path):
        return True
    else:
        return False

def task_initializer() -> dict:
    # initializes the dictionary for the task
    task = {
        'description': ' ',
        'status': ' ',
        'created_at': '',
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

def system_clear() -> None:
    os.system('cls || clear')

def input_task(task_records):
    # ask the user for the task and task status and stores it in a dictionary
    system_clear()
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

    task_status = input_status()

    task_creation_date = dt.datetime.now()
    task_creation_date = task_creation_date.strftime("%d %b %Y (%I:%M %p)")

    is_user_continue = input("\nAre you sure you want to continue? (Y/N): ")
    is_user_continue = is_user_continue.upper()

    task.update({'description': task_description_input, 'created_at': task_creation_date, 'status': task_status})
    records.update({task_id:task})
    
    match is_user_continue:
        case 'Y':
            write_to_file(records)
            return records
        case 'N':
            return records
        
def input_status():
    print("\nENTER TASK STATUS")
    print("[A]: TODO")
    print("[B]: IN PROGRESS")
    print("[C]: DONE")
    
    print("\nENTER CHOICE")
    task_status_user_choice: str = input("-> ")
    task_status_user_choice = task_status_user_choice.upper()
    task_status = task_status_is(task_status_user_choice)

    return task_status

def display_tasks(task_records):
    LOCATION: int = 4
    system_clear()
    header(WIDTH, LOCATION)
    table_header()
    looping_through(task_records)
    input("\nPress ANY KEY to continue...")

def looping_through(task_records):
    for task in task_records.keys():
        id = task
        description = task_records[id]['description']
        status = task_records[id]['status']
        creatied_at = task_records[id]['created_at']
        updated_at = task_records[id]['updated_at']

        print(f"{id:<4}{status:<15}{description:<50}{creatied_at:<25}{updated_at:<25}")

def table_header():
    print(f"{'ID':<4}{'STATUS':<15}{'DESCRIPTION':<50}{'CREATED AT':<25}{'UPDATED AT':<25}")


def write_to_file(records):
    with open('task_records.json', 'w') as f:
        json.dump(records, f, indent=2)

def filter_by(task_records):
    LOCATION: int = 8
    system_clear()
    header(WIDTH, LOCATION)
    print("FILTER BY:")
    print("[A] : TODO")
    print("[B] : IN PROGRESS")
    print("[C] : DONE")
   
    print("\nEnter choice")
    choice = input("-> ")
    choice = choice.upper()

    match choice:
        case 'A':
            filter_records(task_records, STATUS='TODO')
        case 'B':
            filter_records(task_records, STATUS='IN PROGRESS')
        case 'C':
            filter_records(task_records, STATUS='DONE')

def filter_records(task_records, STATUS):
    system_clear()
    header(WIDTH, LOCATION_CODE=5)
    for task in task_records.keys():
        id = task
        if task_records[id]['status'] == STATUS:
            description = task_records[id]['description']
            status = task_records[id]['status']
            creatied_at = task_records[id]['created_at']
            updated_at = task_records[id]['updated_at']
            print(f"{id:<4}{status:<15}{description:<50}{creatied_at:<25}{updated_at:<25}")
    input("\nPress ANY KEY to continue...")
    
def validate_choice(user_choice: str, task_records: dict): 
    # gets the user choice and sends them to the appropriate method
    match user_choice:
        case 'A':
            task_records = input_task(task_records)
        case 'B':
            update_task(task_records)
        case 'C':
            pass
        case 'D':
            display_tasks(task_records)
        case 'E':
            filter_by(task_records)
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
        case 8: 
            LOCATION = "FILTER BY STATUS"

    print(f"." * WIDTH)
    print(f" " * 30 + "TASKMAN - THE CLI-BASED TASK MANAGER")
    print(f" " * 37 + "YOU ARE IN: ", LOCATION)
    print(f"." * WIDTH)

def initialize_dictionary():
    task_records = {}
    if isFileExists():
        with open('task_records.json') as f:
            task_records = json.load(f)
    
    return task_records
def main():
    while True:
        system_clear()
        task_records = initialize_dictionary()
        user_choice = main_menu()
        task_records = validate_choice(user_choice, task_records)

if __name__ == '__main__':
    main()