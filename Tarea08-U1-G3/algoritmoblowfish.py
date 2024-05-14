import os
import time
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

def leer_txt(documento):
    with open(documento, 'r') as doc:
        return doc.read()

# Blowfish utiliza claves de 32 a 448 bits, aquí usamos 64 bits (8 bytes)
def generar_llave():
    return os.urandom(8)  

def texto_cifrado(texto_plano, llave):
    cipher = Blowfish.new(llave, Blowfish.MODE_ECB)
    return cipher.encrypt(pad(texto_plano.encode(), Blowfish.block_size))

def texto_descifrado(texto_cifrado, llave):
    cipher = Blowfish.new(llave, Blowfish.MODE_ECB)
    return unpad(cipher.decrypt(texto_cifrado), Blowfish.block_size).decode()

def contar_caracteres(archivo):
    with open(archivo, 'r') as txt:
        while True:
            caracter = txt.read(1)
            if not caracter:
                break
            print(caracter)



def main():
    tiempo_inicio = time.time()
    documento = '10.txt'
    texto_plano = leer_txt(documento)
    print(f'\nTiempo para leer el archivo: {time.time() - tiempo_inicio} segundos')

    tiempo_inicio = time.time()
    llave = generar_llave()
    print(f'\nClave generada: {llave}')
    print(f'Tiempo para generar la clave: {time.time() - tiempo_inicio} segundos')

    tiempo_inicio = time.time()
    txt_cifrado = texto_cifrado(texto_plano, llave)
    print(f'\nTexto cifrado: {txt_cifrado}')
    print(f'Tiempo para cifrar el texto: {time.time() - tiempo_inicio} segundos')

    tiempo_inicio = time.time()
    txt_descifrado = texto_descifrado(txt_cifrado, llave)
    print(f'\nTexto descifrado: {txt_descifrado}')
    print(f'Tiempo para descifrar el texto: {time.time() - tiempo_inicio} segundos')

    caracter_entrada = contar_caracteres(documento)
    print(f'\nCaracteres en el archivo: {caracter_entrada}')

    caracter_salida = contar_caracteres(txt_cifrado)
    print(f'\nCaracteres en el archivo cifrado: {caracter_salida}')

if __name__ == '__main__':
    main()