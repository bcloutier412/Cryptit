
# Cryptit Guide

## Files in the Program:
- **main.py**: The script that controls the execution of the encryption and decryption processes.
- **cryptit.py**: Contains the core logic for encryption and decryption.
- **utils.py**: Utility functions for handling encryption and decryption operations.
- **text.txt**: The input file containing plain text that will be encrypted.
- **key.txt**: Contains a 128-digit encryption key used by the encryption and decryption algorithm.
- **cipher.txt**: Contains encrypted text from running the encryption algorithm with `key.txt` on `text.txt`.
- **output.txt**: Contains the decrypted text from running the decryption algorithm with `key.txt` on `cipher.txt`.

## Step-by-Step Instructions for Usage:

### Step 1: Set Up Your Environment
Ensure all the necessary Python files (`main.py`, `cryptit.py`, `utils.py`) and the text files (`text.txt`, `key.txt`, `cipher.txt`, `output.txt`) are in the same directory.

### Step 2: Input Preparation
- The `key.txt` file should already contain a **128-digit encryption key**, which the program uses for encryption and decryption. However, you can also use any valid 128-digit encryption key.
- The `text.txt` file should contain the plain text you want to encrypt.

### Step 3: Running the Program for Encryption
1. Ensure that the plain text is available in `text.txt`.
2. Ensure that a **128-digit encryption key** is available in `key.txt`.
3. Run the `main.py` file from the terminal or command line:
   ```bash
   python3 main.py
   ```
   or
   ```bash
   python main.py
   ```
4. The main menu is displayed with three options:
   ```
   1. Encrypt a message
   2. Decrypt a message
   3. Exit Program
   ```
5. Choose option `1` to encrypt a message.
6. You will be prompted to provide the name of the text file you want to encrypt.
   - Provide your own file or use the example file `text.txt`.
7. You will be prompted to provide the name of the key text file.
   - Provide your own file or use the example file `key.txt`.
8. You will be prompted to provide the name of the text file to which the encrypted cipher text will be outputted.
   - Provide your own file or use the example file `cipher.txt`.
9. **Success!** Your message has been encrypted. Please take note of your encryption key and store it safely.

### Step 4: Running the Program for Decryption
1. Ensure that the cipher text is available in `cipher.txt`.
2. Ensure that a **128-digit decryption key** is available in `key.txt`.
3. Run the `main.py` file from the terminal or command line:
   ```bash
   python3 main.py
   ```
   or
   ```bash
   python main.py
   ```
4. The main menu is displayed with three options:
   ```
   1. Encrypt a message
   2. Decrypt a message
   3. Exit Program
   ```
5. Choose option `2` to decrypt a message.
6. You will be prompted to provide the name of the text file you want to decrypt.
   - Provide your own file or use the example file `cipher.txt`.
7. You will be prompted to provide the name of the key text file.
   - Provide your own file or use the example file `key.txt`.
8. You will be prompted to provide the name of the text file to which the decrypted original plain text will be outputted.
   - Provide your own file or use the example file `output.txt`.
9. **Success!** Your message has been decrypted. You will be able to view the decrypted message in your output file.

---

## Notes
- Ensure you do not lose your **128-digit encryption key**; without it, you will not be able to decrypt the message.
- This program expects all file paths to be relative or available in the same directory as the Python scripts.
