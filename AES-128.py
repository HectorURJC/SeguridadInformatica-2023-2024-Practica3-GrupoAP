from Crypto.Cipher import AES

def desencriptar_AES(cifrador, texto_encriptado = "f6994c079e2984d406e90a908076ed69"):
    solucion_desencriptada = cifrador.decrypt(bytes.fromhex(texto_encriptado)) # Se modifica el formato del texto de hexadecimal a bytes.
    return solucion_desencriptada.decode('utf-8') # Lo convertimos al formato estándar utf-8 para que sea entendible y legible para un usuario.

def encriptar_AES(cifrador, texto_desencriptado):
    solucion_encriptada = cifrador.encrypt(texto_desencriptado.encode('utf-8')) # Se modifica el formato del texto de bytes a utf-8.
    return solucion_encriptada.hex() # Lo convertimos a hexadecimal que es el formato correspondiente que tiene el mensaje original.

texto_encriptado = input("Escriba el texto encriptado: \n").strip()
clave = input("Escriba la clave: \n").strip()
iv = input("Escriba el iv: \n").strip()

# Si el input del texto encriptado, clave y/o iv son vacíos, entonces se le pasa el texto encriptado, clave y/o iv del enunciado
if texto_encriptado == "":
    texto_encriptado = "f6994c079e2984d406e90a908076ed69"
if clave == "":
    clave = 'SeguridadInforma' 
if iv == "":
    iv = 'SeguridadInforma' 
clave = bytes(clave, 'utf-8') # Se modifica el string a un array de bytes
iv = bytes(iv, 'utf-8') # Se modifica el string a un array de bytes

# AES.new(clave, AES.MODE_CBC, iv) no se le puede asignar a una variable global porque no
# se puede cifrar una vez que se ha usado la función decrypt() y lo mismo con encrypt()
solucion_desencriptada = desencriptar_AES(AES.new(clave, AES.MODE_CBC, iv), texto_encriptado)
solucion_encriptada = encriptar_AES(AES.new(clave, AES.MODE_CBC, iv), solucion_desencriptada)

print("Solución desencriptada: " + solucion_desencriptada)
print("Solución encriptada: " + solucion_encriptada)
