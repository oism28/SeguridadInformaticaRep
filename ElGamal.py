# Algoritmo ElGamal
# Seguridad Informática

import random
import Crypto.Util.number

#Usamos el primo estándar RFC 3526 de 1536 bit MODP group
p = int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF", 16)

# Usamos eñl generado estandar de RFC 3526
g = 2

# Generar las llaves privadas
x = random.getrandbits(256) # Clave privada
y = pow (g,x,p) # Clave Pública de Bob -> y = g^x mod p

# Generar las llaves de Bob
y = pow(g, x, p)
print("\n", "Llave Privada de bob", x)
print("\n", "Llave de Bob: (p, g, y):" ,p, g, y)

# Generar las llaves de Alice
k = random.getrandbits(256) # Clave privada
a = pow (g,k,p) # Clave Pública de Alice -> a = g^k mod p

print("\n", "Llave Privada de bob", k) 
print("\n", "Llave de Bob: (p, g, y):" ,p, g, a)
 
# Creamos el Mensaje Original
M = 850
print("\n", "Mensaje original:", M)

# Cifrado del Mansaje
# b = ((y^k)*M) 
b = (pow(y,k,p)*M) % p

print("\n", "Mensaje Cifrado:", b)

# Descifrando el mensaje
M1 = (b * Crypto.Util.number.inverse(pow(a,x,p),p)) % p

print("\n", "Mensaje descifrado:", M1)