#Actividad 1
#Omar Serrano
import hashlib
import random

p = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF",16)
g = 2

# Inicio
print("\n", "******************************")
print("\n", "Variables Públicas compartidas")
print("\n", "Número primo compartido públicamente RFC3625:", p)
print("\n", "Número base compartido publicamente", g)

# Generar los números secretos de Alice y Bob
# Estos dos números son lo oculto, todo lo demás es público a excepció de este par de números aleatorios que tiene cada uno
sAlice = random.getrandbits(256) #a
sBob = random.getrandbits(256) #b
sEveB = random.getrandbits(256) #c
sEveA = random.getrandbits(256) #d

print("\n", "Número Secreto Alice:", sAlice)
print("\n", "Número Secreto Bob:", sBob)
print("\n", "Número Secreto Eve a Bob:", sEveB)
print("\n", "Número Secreto Eve a Alice:", sEveA)

# Alice manda mensaje a Bob (Lo intercepta Eve) -> A = g^a mod p
A = pow(g, sAlice, p)
print("\n", "Mensaje de Alice a Eve:", A)

# Eve calcula la llave secreta compartida -> s1 = B^a mod p
s1 = pow(A, sEveA, p)
print("\n", "Llave secreta compartida: ", s1)

# Eve manda mensaje a Bob -> C= g^c mod p
bEve = pow(g, sEveB, p)
print("\n", "Mensaje de Eve a Bob:", bEve)

# Bob calcula la llave secreta compartida -> s1 = A^b mod p
s2 = pow(bEve, sBob, p)
print("\n", "Llave secreta compartida: ", s2)

# Bob manda mensaje a Alice (Lo intercepta Eve)-> B = g^b mod p
B = pow(g, sBob, p)
print("\n", "Mensaje de Bob a Eve:", B)

# Eve calcula la llave secreta compartida -> s1 = B^a mod p
s3 = pow(B, sEveA, p)
print("\n", "Llave secreta compartida: ", s3)

# Eve manda mensaje a Alice -> D= g^d mod p
aEve = pow(g, sEveA, p)
print("\n", "Mensaje de Eve a Alice:", aEve)

# Alice calcula la llave secreta compartida -> s1 = B^a mod p
s4 = pow(aEve, sAlice, p)
print("\n", "Llave secreta compartida: ", s4)

########################################################################################
print("\n", "******************************************************************************************")









# Comparamos las llaves secretas
h1 = hashlib.sha512(int.to_bytes(s1, length = 1024, byteorder = 'big')).hexdigest()
h2 = hashlib.sha512(int.to_bytes(s4, length = 1024, byteorder = 'big')).hexdigest()

print("\n", "h1:", h1)
print("\n", "h2:", h2)

if(h1 == h2):
    print("\n", "TRUE", "\n")
else:
    print("\n", "FALSE", "\n")