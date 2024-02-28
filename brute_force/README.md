![image](https://github.com/Ravenneo/Caesar/assets/41577767/2e129d7b-6108-44ca-bcb8-51debf8c904f)
(image generated with Copilot)

# ZipCrack Python Scripts

This repository contains Python scripts for password-cracking password-protected ZIP archives. There are two main scripts available:

1. **ZipCrack.py**
    - This script utilizes multithreading to perform a brute-force attack on a password-protected ZIP archive.
    - It takes a ZIP archive file (`-z`) and a password file (`-p`) as input.
    - To execute, use the following command:
        ```bash
        python ZipCrack.py -z <zipfile.zip> -p <passwordfile.txt>
        ```
    - The script reads passwords from the specified file and tests them concurrently using multithreading. If a password is found, it is printed, otherwise, a message is displayed indicating that the password was not found.

2. **Zip_basic_brute.py**
    - This is a basic version of the ZIP password-cracking script.
    - It also takes a ZIP archive file (`-z`) and a password file (`-p`) as input.
    - To execute, use the following command:
        ```bash
        python Zip_basic_brute.py -z <zipfile.zip> -p <passwordfile.txt>
        ```
    - This script reads passwords from the specified file and tests them sequentially. If a password is found, it is printed, otherwise, a message is displayed indicating that the password was not found.

Additionally, there is a `password.txt` file included, which contains a dictionary of words for dictionary attacks.

## Instructions

### Creating a Password-Protected ZIP Archive:
1. **Create Your Files:** Prepare the files you want to include in the ZIP archive. Ensure they are in the same directory as your terminal session.
2. **Open a Terminal:** Open a terminal on your system.
3. **Navigate to the Directory:** Use the `cd` command to navigate to the directory containing your files.
4. **Create the ZIP Archive:** Use the `zip` command to create a password-protected ZIP archive. Replace `archive_name.zip` with the desired name for your archive and specify the names of the files you want to include:
    ```bash
    zip -e archive_name.zip file1 file2 file3
    ```
    You will be prompted to enter and verify a password for the archive.

### Executing the Password-Cracking Script:
1. **Save the Script:** Save the Python script (e.g., `ZipCrack.py` or `Zip_basic_brute.py`) to a directory of your choice.
2. **Open a Terminal:** Open a terminal on your system.
3. **Navigate to the Script's Directory:** Use the `cd` command to navigate to the directory where your Python script is located.
4. **Run the Script:** Execute the script using Python, replacing `target.zip` with the path to the ZIP archive you created and `passwords.txt` with the path to a text file containing potential passwords:
    ```bash
    python ZipCrack.py -z target.zip -p passwords.txt
    ```
    The script will attempt to crack the password for the ZIP archive. If successful, it will display the found password; otherwise, it will notify you that the password was not found.

**Note:** Use this script responsibly and only on systems and files for which you have explicit permission to test or access. Unauthorized use of password-cracking tools can have legal and ethical consequences.
