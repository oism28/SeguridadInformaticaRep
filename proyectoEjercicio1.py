import Crypto.Util.number # type: ignore
import hashlib
import random

e = 65357

pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nA = pA * qA
print("\n", "RSA Llave pública de Alice:", nA)

#pB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
#qB = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

#nB = pB * qB
#print("\n", "RSA nBob:", nB)

phiA = (qA - 1) * (pA - 1)
dA = Crypto.Util.number.inverse(e, phiA)

print("\n", "RSA Llave privada Alice dA:", dA)

#phiB = (qB - 1) * (pB - 1)
#dB = Crypto.Util.number.inverse(e, phiB)

#print("\n", "RSA Llave privada Alice dA:", dB)

mensaje = "Hola mundo!"

print(mensaje)

hM = int.from_bytes(hashlib.sha256(mensaje.encode('utf-8')).digest(),byteorder='big')
print("\n", "HASH de hM:", hex(hM))

sA = pow(hM, dA, nA)
print("\n", "Firma:", sA)

hM1 = pow(sA,e,nA)
print("\n", "HASH de hM1", hex(hM1))
if(hM1==hM):
    print("Firma valida")
else:
    print("Firma no valida")

#############################################################################################

def calcular_hash_pdf(ruta_pdf, algoritmo="sha256", tamano_bloque=65536):
    hasher = hashlib.new(algoritmo)
    with open(ruta_pdf, "rb") as archivo:
        while bloque := archivo.read(tamano_bloque):
            hasher.update(bloque)
    return hasher.hexdigest()

ruta_pdf = "NDA.pdf"
hash_resultado = calcular_hash_pdf(ruta_pdf,"sha256")
print("Hash SHA-256:", hash_resultado)
###############################################################################################
print(hashlib.sha256(open("NDA.pdf", "rb").read()).hexdigest())