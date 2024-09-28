from utilsFile import *


def caesar_cipher(message, shift=0):
    """
    Encrypts or decrypts a message using a modified Caesar cipher, where only every third letter is shifted.

    Args:
        message (str): The message to be encrypted or decrypted.
        shift (int): The number of positions to shift the alphabet by.
                     A positive shift will encrypt, while a negative shift will decrypt.

    Returns:
        str: The encrypted or decrypted message.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_message = ""
    letter_count = 0  # Keeps track of the letters to apply the shift every third letter

    # Check if the message ends with a newline and remove it temporarily
    has_newline = message.endswith("\n")
    if has_newline:
        message = message[:-1]  # Remove the newline

    for letter in message:
        if letter.isalpha():
            letter_count += 1
            # Shift only every X amount of letters
            if shift != 0 and letter_count % shift == 0:
                # Preserve the case of the letter
                is_upper = letter.isupper()
                letter = letter.lower()

                # Find the position of the letter in the alphabet
                position = alphabet.index(letter)

                # Perform the shift
                new_position = (position + shift) % 26

                # Get the new letter from the alphabet
                new_letter = alphabet[new_position]

                # Convert back to uppercase if the original was uppercase
                if is_upper:
                    new_letter = new_letter.upper()

                shifted_message += new_letter
            else:
                # If it's not the third letter, add it unchanged
                shifted_message += letter
        else:
            # If the character is not a letter, add it unchanged
            shifted_message += letter

    # Add the newline back if it was originally present
    if has_newline:
        shifted_message += "\n"

    return shifted_message


def pair_swap_cipher(message):
    """
    Encrypts or decrypts a message by swapping every two consecutive characters.

    If the message has an odd number of characters, the last character remains unchanged.

    Args:
        message (str): The message to be encrypted or decrypted.

    Returns:
        str: The encrypted or decrypted message.
    """
    swapped_message = ""

    # Check if the message ends with a newline and remove it temporarily
    has_newline = message.endswith("\n")
    if has_newline:
        message = message[:-1]  # Remove the newline

    i = 0
    while i < len(message):
        if i + 1 < len(message):
            # Swap the current letter with the next one
            swapped_message += message[i + 1] + message[i]
            i += 2
        else:
            # If there's an odd letter at the end, just append it
            swapped_message += message[i]
            i += 1

    # Add the newline back if it was originally present
    if has_newline:
        swapped_message += "\n"

    return swapped_message


def group_swap_cipher(message, group_num=2):
    """
    Encrypts or decrypts a message by swapping characters in blocks of 'x' consecutive characters.

    If the message has fewer than 'x' characters remaining at the end, they remain unchanged.

    Args:
        message (str): The message to be encrypted or decrypted.
        x (int): The number of characters in each swap group. Default is 2 (pair swap).

    Returns:
        str: The encrypted or decrypted message.
    """
    swapped_message = ""

    # Check if the message ends with a newline and remove it temporarily
    has_newline = message.endswith("\n")
    if has_newline:
        message = message[:-1]  # Remove the newline

    i = 0
    while i < len(message):
        # If there are at least x characters left, swap the next x characters
        if i + group_num <= len(message):
            group = message[i:i + group_num]
            swapped_message += group[::-1]  # Reverse the group of x characters
            i += group_num
        else:
            # If there are fewer than x characters left, add them unchanged
            swapped_message += message[i:]
            break

    # Add the newline back if it was originally present
    if has_newline:
        swapped_message += "\n"

    return swapped_message


def encrypt_message():
    """
    Encrypts the contents of a text file and outputs an encrypted text file.

    - Reads the contents of a text file (line by line).
    - Asks the user to provide a key for encryption, which determines the sequence
      of ciphers to apply.
    - Applies a series of ciphers (Caesar, Atbash, Pair Swap) to each line of the text.
    - Outputs the encrypted message to a new text file.

    The sequence of ciphers is based on a user-supplied key, where each digit of the key
    corresponds to a specific cipher.

    Returns:
        None
    """
    # Get the text file contents from the user input
    message_list = read_text_file_contents(prompt_message="Input text file [ ex: textFile.txt ]: ")

    # Check for errors and return
    if message_list is None:
        return

    # Get key from user input
    key = get_key_from_file()

    # Check for invalid key
    if key is None:
        return

    # Convert integer into a bucket of digits
    key_buckets = [int(digit) for digit in str(key)]

    # The Cipher methods that are available to use
    encryption_actions = [caesar_cipher, pair_swap_cipher, group_swap_cipher]

    # Generating tasks list from key
    encryption_actions_tasks = create_encrytion_actions_tasks(key_buckets, len(encryption_actions))

    # Iterating through task list and applying cipher to the messages
    for action in encryption_actions_tasks:
        for index in range(len(message_list)):
            if encryption_actions[action["task"]] == caesar_cipher:
                # Call caesar_cipher with the shift argument
                message_list[index] = caesar_cipher(message_list[index], shift=action["value"])
            if encryption_actions[action["task"]] == group_swap_cipher:
                message_list[index] = group_swap_cipher(message_list[index], group_num=action["value"])
            else:
                # Call other ciphers without the shift argument
                message_list[index] = encryption_actions[action["task"]](message_list[index])

    # Open text file and off load message_list
    write_to_text_file(message_list, prompt_message="Output cipher text file [ ex: cipherFile.txt ]: ")

    print("\nSuccess! Your message has been encrypted. You will be able to view the encrypted message in your output file. Please take note of your encryption key and store it safely, as it will be required to decrypt the message.\n")

    continue_checkpoint()

    return


def decrypt_message():
    """
    Decrypts the contents of an encrypted text file based on a user-provided key.

    - Reads the contents of an encrypted text file (line by line).
    - Asks the user to provide the key used during encryption.
    - Uses the key to determine the sequence of ciphers applied and reverses them
      (e.g., reversing the Caesar cipher by using a negative shift).
    - Outputs the decrypted message to a new text file.

    Returns:
        None
    """
    message_list = read_text_file_contents(prompt_message="Input cipher text file [ ex: cipherFile.txt ]: ")

    # Check for errors and return
    if message_list is None:
        return

    # Get key from user input
    key = get_key_from_file()

    # Check for invalid key
    if key is None:
        return

    # Convert integer into a bucket of digits
    key_buckets = [int(digit) for digit in str(key)]

    # The Cipher methods that are available to use
    encryption_actions = [caesar_cipher, pair_swap_cipher, group_swap_cipher]

    # Generating tasks list from key
    encryption_actions_tasks = create_encrytion_actions_tasks(key_buckets, len(encryption_actions))

    # Iterating through task list in reverse and applying cipher to decode the messages
    for action in reversed(encryption_actions_tasks):
        for index in range(len(message_list)):
            if encryption_actions[action["task"]] == caesar_cipher:
                # Call caesar_cipher with the shift argument
                message_list[index] = caesar_cipher(message_list[index], shift=(action["value"] * -1))
            if encryption_actions[action["task"]] == group_swap_cipher:
                message_list[index] = group_swap_cipher(message_list[index], group_num=action["value"])
            else:
                # Call other ciphers without the shift argument
                message_list[index] = encryption_actions[action["task"]](message_list[index])

    # Open text file and off load message_list
    write_to_text_file(message_list, prompt_message="Ouput text file [ ex: ouputFile.txt ]: ")

    print("\nSuccess! Your message has been decrypted. You will be able to view the decrypted message in your ouput file.\n")

    continue_checkpoint()

    return
