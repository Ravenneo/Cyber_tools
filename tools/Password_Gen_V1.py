import string
import random

longitud = int(input("how long?"))

caracteres = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(caracteres) for i in range(longitud))

print("the password is: " + password)

