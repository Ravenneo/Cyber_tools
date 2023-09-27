def caesar(message, key, mode):
    LETTERS = 'abcdefghijklmnñopqrstuvwxyz '  
    translated = ''

    for i in message:
        if i == ' ':
            translated += ' '  # Si el carácter es un espacio, simplemente añádelo al resultado sin cifrarlo ni descifrarlo.
        else:
            templetter = LETTERS.find(i)
            if mode == 'encrypt':
                templetter = (templetter + key) % 27
            elif mode == 'decrypt':
                templetter = (templetter - key) % 27
                if templetter < 0:
                    templetter += 27
            translated += LETTERS[templetter]
    return translated


mensaje_cifrado = caesar("come coquinas", 3, 'encrypt') #Añade el mensaje a codificar
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = caesar("froh frtxlpdv", 3, 'decrypt') #añade mensaje a decodificar
print("Mensaje descifrado:", mensaje_descifrado)
