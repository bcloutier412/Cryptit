from cryptitFile import *
from utilsFile import *

def main():
    """
    Main driver function that serves as the entry point to the program.

    The function continuously displays a menu to the user, accepts their input, and
    processes their request based on the selected menu option. Depending on the user's 
    choice, it either performs message encryption, decryption, or exits the program.
    
    Menu Options:
    1. Encrypt a message
    2. Decrypt a message
    3. Exit the program
    
    The function executes the following steps:
    
    1. Displays the menu using `print_menu()` (assumed to be imported from utils).
    2. Retrieves the user's menu selection using `get_menu_selection()` (assumed to be imported from utils).
    3. Calls `encrypt_message()` if the user selects option 1 (assumed to be imported from cryptit).
    4. Calls `decrypt_message()` if the user selects option 2 (assumed to be imported from cryptit).
    5. Exits the program if the user selects any other option.
    """
    while True:
        # Output menu to terminal
        print_menu()

        # Get user menu selection
        user_menu_selection = get_menu_selection()
            
        # Processing user menu selection
        if user_menu_selection == '1':
            encrypt_message()
        elif user_menu_selection == '2':
            decrypt_message()
        else:
            break
        


if __name__ == "__main__":
    main()
