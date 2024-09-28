import os
import platform
import sys


def clear_terminal():
    """
    Clears the terminal screen based on the operating system.

    If the system is Windows, it uses 'cls', otherwise 'clear' for Linux/macOS.
    """
    if platform.system() == "Windows":
        os.system("cls")  # For Windows
    else:
        os.system("clear")  # For Linux and macOS


def print_menu():
    """
    Prints the main menu of the program to the terminal, displaying options for
    encrypting, decrypting, or exiting the program.

    This function also clears the terminal before printing the menu using 'clear_terminal'.
    """
    clear_terminal()
    print("=========================================")
    print(
        r"""
   ___                   _     ___  _   
  / __| _ _  _  _  _ __ | |_  |_ _|| |_ 
 | (__ | '_|| || || '_ \|  _|  | | |  _|
  \___||_|   \_, || .__/ \__| |___| \__|
             |__/ |_|                   
            """
    )
    print("=========================================")
    print()
    print("   **  Please choose a menu option  **")
    print()
    print("       1. Encrypt a message ----->")
    print("       2. Decrypt a message <-----")
    print("       3. Exit Program       [ X ]")
    print()


def get_menu_selection():
    """
    Prompts the user to select a menu option and validates the input.

    Handles invalid input, keyboard interrupts, and returns the selected menu option
    as an integer. If an error or interrupt occurs, the program prints an error
    message or exits cleanly.

    Returns:
        int: The menu option selected by the user, or None if the process is interrupted.
    """
    user_menu_selection = None

    while user_menu_selection == None:
        try:
            user_menu_selection = input("Menu selection: ")
            print()
        except ValueError:
            print("\n[ Error ] An invalid input was provided please try again.\n")

        except KeyboardInterrupt:
            print("\n\n[ Bye ]")
            return

        except Exception:
            print("\n[ Error ] An error occured please restart the program.\n")
            return

    return user_menu_selection


def read_text_file_contents(prompt_message="Input [ example.txt ]: "):
    """
    Reads and returns the contents of a text file provided by the user.

    The function ensures the file exists and is a text file by checking its extension
    and existence. In case of errors (e.g., file not found, I/O errors), the user is
    prompted to retry or exit.

    Args:
        prompt_message (str): A message to prompt the user for a file input.

    Returns:
        list[str]: The contents of the text file as a list of lines, or None if the user exits.
    """
    while True:
        try:
            file_path = input(prompt_message)

            # Check if the file has a .txt extension
            if not file_path.lower().endswith(".txt"):
                print(f'\n[ Error ] {file_path} is not a .txt file.\n')
                if not prompt_retry():
                    return None
                continue

            with open(file_path, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"\n[ Error ] The file '{file_path}' was not found. Please try again.\n")
        except IOError:
            print("\n[ Error ] An I/O error occurred.\n")
        except KeyboardInterrupt:
            print("\n\n[ Bye ]")
            sys.exit()
        except Exception:
            print("\n[ Error ] Uh oh, something went wrong.\n")

        # Ask the user if they want to try again
        if not prompt_retry():
            return None


def write_to_text_file(message_list, prompt_message="Output [ example.txt ]: "):
    """
    Writes a list of strings to a text file provided by the user.

    The function ensures the output file has a .txt extension and handles errors
    like I/O failures. The user is prompted to retry in case of errors.

    Args:
        message_list (list[str]): The list of strings to write to the text file.
        prompt_message (str): A message to prompt the user for the output file name.

    Returns:
        None or the result of writing the message to the file.
    """
    while True:
        try:
            file_path = input(prompt_message)

            # Check if the file has a .txt extension
            if not file_path.lower().endswith(".txt"):
                print(f'\n[ Error ] {file_path} is not a .txt file.\n')
                if not prompt_retry():
                    return None
                continue

            with open(file_path, "w") as file:
                return file.writelines(message_list)
        except IOError:
            print("\n[ Error ] An I/O error occurred.\n")
        except KeyboardInterrupt:
            print("\n\n[ Bye ]")
            sys.exit()
        except Exception:
            print("\n[ Error ] Uh oh, something went wrong.\n")

        # Ask the user if they want to try again
        if not prompt_retry():
            return None


def prompt_retry():
    """
    Asks the user whether they want to try again and processes the response.

    Returns:
        bool: True if the user wants to retry, False otherwise. Exits the program if the user declines.
    """
    try:
        user_input = input("Would you like to try again? Y/N: ").strip().lower()
        if user_input == "y":
            print()
            return True
        else:
            print("\nExiting...\n")
            return False
    except KeyboardInterrupt:
        print("\n\n[ Bye ]")
        sys.exit()

def get_key_from_file():
    """
    Prompts the user to input a file path for the encryption key, reads the key from the file,
    and validates that the key is 128 digits long. Handles invalid inputs, missing files, 
    and other potential errors.

    Returns:
        str: The valid encryption key from the file, or None if the user exits.
    """
    while True:
        try:
          file_path = input("Key text file [ ex: keyFile.txt ]: ").strip()

          # Check if the file has a .txt extension
          if not file_path.lower().endswith(".txt"):
              print(f'\n[ Error ] {file_path} is not a .txt file.\n')
              if not prompt_retry():
                  return None
              continue
              
          with open(file_path, 'r') as file:
                key = file.read().strip()  # Remove extra spaces or newlines

                if len(key) == 128 and key.isdigit() and int(key) > int('1' * 128):
                    return key
                else:
                    print(
                        "\n[ Error ] The key must be exactly 128 digits long, contain only digits, and not only include 1's and 0's.\n"
                    )

        except FileNotFoundError:
            print(f"\n[ Error ] The file '{file_path}' was not found. Please try again.\n")
        except ValueError:
            print("\n[ Error ] The key must be a numeric string of 128 digits.\n")
        except KeyboardInterrupt:
            print("\n\n[ Bye ]")
            sys.exit()
        except Exception:
            print("\n[ Error ] Uh oh, something went wrong.\n")

        # Ask the user if they want to try again
        if not prompt_retry():
            return None



def create_encrytion_actions_tasks(key_buckets, num_of_encryption_actions):
    """
    Creates a list of encryption tasks based on the distribution of the key buckets.

    The function iterates over the key buckets (representing actions) and creates a list
    of tasks where each task has a modulo-based assignment. It continues processing
    until all tasks are done.

    Args:
        key_buckets (list[int]): A list of integers representing the distribution of encryption operations.

    Returns:
        list[dict]: A list of dictionaries representing the encryption tasks and their modulo-based assignments.
    """
    encrytion_actions_list = []
    pointer = 0
    has_done_operation_in_this_iteration = False

    while True:
        if key_buckets[pointer] > 0:
            encrytion_actions_list.append({"task": pointer % num_of_encryption_actions, "value": key_buckets[pointer]})
            key_buckets[pointer] -= 1
            has_done_operation_in_this_iteration = True

        if pointer == len(key_buckets) - 1:
            if has_done_operation_in_this_iteration is False:
                return encrytion_actions_list

            pointer = 0
            has_done_operation_in_this_iteration = False
        else:
            pointer += 1


def continue_checkpoint():
    try:
        if input("Press 'enter' to continue or type 'x' to exit the program: ").strip().lower() == "x":
            print("\n\n[ Bye ]")
            sys.exit()
    except KeyboardInterrupt:
        print("\n\n[ Bye ]")
        sys.exit()