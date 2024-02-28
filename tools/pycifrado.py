def encrypt(key, message):
    ciphertext = [''] * key
    for x in range(key):
        pointer = x

        while pointer < len(message):
              ciphertext[x] += message[pointer]
              pointer += key
    return ''.join(ciphertext)
def main():
      message = input('escribe mensaje: ')
      key = int(input('elige código'))
      print(encrypt(key, message))

if __name__ == '__main__':
    main()
