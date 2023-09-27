# Importa la biblioteca string para usar caracteres predefinidos
import string

# Define la función de cifrado César
def caesar(message, key, mode):
    # Define un conjunto de caracteres que incluye letras acentuadas, símbolos y números
    LETTERS = string.ascii_lowercase + 'áéíóúüñABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚÜÑ0123456789?!., '
    translated = ''  # Inicializa una cadena vacía para almacenar el resultado

    # Itera sobre cada carácter en el mensaje
    for char in message:
        if char in LETTERS:
            # Si el carácter está en el conjunto de caracteres definido
            char_index = LETTERS.index(char)  # Obtiene el índice del carácter en el conjunto
            if mode == 'encrypt':
                # Cifra el carácter sumando la clave y calculando el índice resultante
                translated_char_index = (char_index + key) % len(LETTERS)
            elif mode == 'decrypt':
                # Descifra el carácter restando la clave y calculando el índice resultante
                translated_char_index = (char_index - key) % len(LETTERS)
            # Agrega el carácter correspondiente al resultado
            translated += LETTERS[translated_char_index]
        else:
            # Si el carácter no está en el conjunto de caracteres, lo deja sin cambios
            translated += char

    return translated

# Define la función principal del programa
def main():
    print("Bienvenido al cifrador César")
    
    while True:
        # Pregunta al usuario si quiere cifrar o descifrar
        mode = input("¿Quieres codificar o decodificar? (c/d): ").lower()
        if mode not in ['c', 'd']:
            print("Por favor, ingresa 'c' para codificar o 'd' para decodificar.")
            continue

        try:
            # Pide al usuario que ingrese el número de clave
            key = int(input("Ingresa el número de código: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        # Pide al usuario que ingrese el mensaje
        message = input("Ingresa el mensaje: ")

        if mode == 'c':
            # Si el usuario eligió cifrar, llama a la función de cifrado y muestra el resultado
            result = caesar(message, key, 'encrypt')
            print("Mensaje cifrado:", result)
        else:
            # Si el usuario eligió descifrar, llama a la función de cifrado con el modo 'decrypt' y muestra el resultado
            result = caesar(message, key, 'decrypt')
            print("Mensaje descifrado:", result)

        # Pregunta al usuario si desea realizar otra operación
        again = input("¿Deseas realizar otra operación? (s/n): ").lower()
        if again != 's':
            break

# Comprueba si el script se está ejecutando como programa principal
if __name__ == "__main__":
    main()
