# Ejercicio de cifrado simétrico AES usando el algoritmo de FERNET

#Importando la librería 
from cryptography.fernet import Fernet

# Generar llave de cifrado
key = Fernet.generate_key()
print("Llave: ", key)

# Mensaje a cifrar
message = "Mensaje secreto".encode('utf-8')
print('Mensaje original', message)

# Cifrar el mensaje
f = Fernet(key)
mensaje_cifrado = f.encrypt(message)
print('Mensaje Cifrado: ', mensaje_cifrado)

# Descifrar el mensaje
mensaje_descifrado = f.decrypt(mensaje_cifrado)
print('mensaje descifrado: ', mensaje_descifrado)