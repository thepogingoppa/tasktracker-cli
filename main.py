"""
CLI-BASED TASK-MANAGER

PROGRAM DESCRIPTION: This is a CLI-based task manager that will ADD, UPDATE, TRACK and
DELETE tasks and then store them in a JSON file.

DATE STARTED: 04 APR 2025
DATE FINISHED: -TBA-
"""

def main_menu() -> str:
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

def validate_choice(user_choice: str): 
    match user_choice:
        case 'A':
            pass
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

def error_validation(error_code: int):
    match error_code:
        case 100:
            print(f"ERROR {error_code}: Invalid Choice! Choose between A - F")
            input("Press ANY KEY to continue...")
            

def header(WIDTH: int, LOCATION_CODE: int) -> None:

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
    user_choice = main_menu()
    validate_choice(user_choice)

if __name__ == '__main__':
    main()