# Omar Isaac Serrano Martinez
# Ejercicio 2 Primer Parcial
# Seguridad Informática y Análisis Forénse

import Crypto.Util.number # type: ignore
import hashlib
import random

e = 65357

# Creación de llave pública de Alice
pA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nA = pA * qA
print("\n", "RSA Llave pública de Alice:", nA)

# Creación de llave pública de la AC
pAc = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)
qAc = Crypto.Util.number.getPrime(1024, randfunc=Crypto.Random.get_random_bytes)

nAc = pAc * qAc
print("\n", "RSA Pública de AC:", nAc)

# Creación de la llave privada de Alice
phiA = (qA - 1) * (pA - 1)
dA = Crypto.Util.number.inverse(e, phiA)

print("\n", "RSA Llave privada Alice:", dA)

# Creación de la llave privada de la AC
phiAc = (qAc - 1) * (pAc - 1)
dAc = Crypto.Util.number.inverse(e, phiAc)

print("\n", "RSA Llave privada AC dAc:", dAc)

# Sacamos el hash del documento original
hM = int(hashlib.sha256(open("NDA.pdf", "rb").read()).hexdigest(),16)
print("\n", "HASH del PDF:", hex(hM))

sA = pow(hM, dA, nA)
print("\n", "Firma de Alice:", sA)

hM1 = pow(sA,e,nA)
print("\n", "HASH de hM1", hex(hM1))

# Verificamos que el HASH sea el mismo
if(hM1==hM):
    print("Firma valida")
else:
    print("Firma no valida")

# La AC a verificado que la firma es de Alice
# La AC ahora firma el documento para mandarlo a Bob
sAc = pow(hM, dAc, nAc)
print("\n", "Firma de la AC:", sAc)

# Bob lo descifra usando la llave púlica de la Ac
hM1c = pow(sAc,e,nAc)
print("\n", "HASH de hM1c", hex(hM1))

if(hM1c==hM):
    print("Firma valida")
else:
    print("Firma no valida")