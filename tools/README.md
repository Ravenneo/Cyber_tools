# Cyber Tools

This repository contains a set of Python scripts for various cybersecurity tasks.

## Password_Gen_V1.py

### Description:
This script generates a random password based on user-defined criteria. It prompts the user for the desired password length and creates a strong password by combining letters (both uppercase and lowercase), digits, and special characters.

### Usage:
```python
import string
import random

longitud = int(input("how long?"))

caracteres = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(caracteres) for i in range(longitud))

print("the password is: " + password)


## pycifrado.py

This Python script provides a basic encryption function. It takes a message and a numerical key as input and encrypts the message using a simple encryption algorithm.

### Usage

1. Run the script by executing the following command in your terminal:

   ```bash
   python pycifrado.py

####Script Details
encrypt Function

The encrypt function takes two parameters - **key** and **message**. It creates a ciphertext by iterating over the message and appending characters at specific intervals determined by the key.

**Running the Script**

The main function is responsible for taking user input, calling the encrypt function, and displaying the encrypted result.

```
def encrypt(key, message):
    ciphertext = [''] * key
    for x in range(key):
        pointer = x

        while pointer < len(message):
            ciphertext[x] += message[pointer]
            pointer += key
    return ''.join(ciphertext)

def main():
    message = input('Enter message: ')
    key = int(input('Choose code: '))
    print(encrypt(key, message))

if __name__ == '__main__':
    main()```
