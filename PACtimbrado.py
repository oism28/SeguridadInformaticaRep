import requests

# Configurar la URL del PAC (Ejemplo: SW Sapien, FEL México, Edicom)
url_pac = "https://services.test.sw.com.mx/cfdi33/stamp/v4"

# Cargar el XML firmado
with open("cfdi_firmado.xml", "rb") as xml_file:
    xml_data = xml_file.read()

# Enviar el XML para timbrado
response = requests.post(url_pac, files={"xml": ("cfdi.xml", xml_data)}, headers={"Authorization": "Bearer TOKEN_DE_PRUEBA"})

# Verificar la respuesta
if response.status_code == 200:
    with open("cfdi_timbrado.xml", "wb") as f:
        f.write(response.content)
    print("CFDI timbrado correctamente.")
else:
    print("Error al timbrar:", response.text)
