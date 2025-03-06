from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Cargar la llave privada (.key)
with open("CSD.key", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=  # Escribir la contraseña real de la clave
    )

# Cargar el XML
with open("cfdi.xml", "rb") as xml_file:
    xml_data = xml_file.read()

# Firmar el XML
firma = private_key.sign(
    xml_data,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Guardar la firma en un archivo
with open("cfdi_firmado.xml", "wb") as f:
    f.write(firma)

print("XML firmado correctamente.")
