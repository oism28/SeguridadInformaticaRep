import Crypto.Util.number # type: ignore
import hashlib
import random

e = 65357

# Generar las claves de Alice
pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nA = pA * qA
print("\n", "RSA Llave pública de Alice:", nA)

phiA = (qA - 1) * (pA - 1)
dA = Crypto.Util.number.inverse(e, phiA)

print("\n", "RSA Llave privada Alice dA:", dA)

# Generar las claves de Bob
pB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nB = pB * qB
print("\n", "RSA Llave pública de Bob:", nB)

phiB = (qB - 1) * (pB - 1)
dB = Crypto.Util.number.inverse(e, phiB)

print("\n", "RSA Llave privada de Bob dB:", dB)

# Mensaje original
mensaje = random.getrandbits(1050)
print("\n", "Mensaje original:", mensaje)

# Dividir el mensaje en partes de 128 caracteres
def dividir_numero(mensaje, tamaño=128):
    numero = str(mensaje)
    partes = [numero[i:i + tamaño] for i in range(0, len(numero), tamaño)]
    return partes

partes = dividir_numero(mensaje)

# Cifrar el mensaje con la clave pública de Bob
def cifrar_mensaje(partes, nA, e):
    return [pow(int(parte), e, nA) for parte in partes]

partes_cifradas = cifrar_mensaje(partes, nA, e)

# Descifrar el mensaje con la clave privada de Bob
def descifrar_mensaje(partes_cifradas, nA, dA):
    return [pow(parte_cifrada, dA, nA) for parte_cifrada in partes_cifradas]

partes_descifradas = descifrar_mensaje(partes_cifradas, nA, dA)

# Reconstruir el mensaje original
def reconstruir_mensaje(partes_descifradas):
    return ''.join(map(str, partes_descifradas))

mensaje_descifrado = reconstruir_mensaje(partes_descifradas)
print("\n", "Mensaje descifrado:", mensaje_descifrado)

# Calcular el hash del mensaje original y del mensaje descifrado
def calcular_hash(mensaje):
    return hashlib.sha256(str(mensaje).encode()).hexdigest()

hM = calcular_hash(mensaje)
print("\n", "Hash original (h(M)):", hM)

hM1 = calcular_hash(mensaje_descifrado)
print("\n", "Hash descifrado (h(M')):", hM1)

# Comparar los hashes
if hM == hM1:
    print("\n", "El mensaje es auténtico: h(M) = h(M')")
else:
    print("\n", "El mensaje no es auténtico: h(M) ≠ h(M')")