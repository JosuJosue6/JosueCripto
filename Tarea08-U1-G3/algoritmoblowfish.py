import os
import time
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

def leer_txt(documento):
    with open(documento, 'r') as doc:
        return doc.read()

# Blowfish utiliza claves de 32 a 448 bits, aquí usamos 64 bits (8 bytes)
def generar_llave():
    return os.urandom(56)  

def texto_cifrado(texto_plano, llave):
    texto_plano = str(texto_plano)
    cifrar = Blowfish.new(llave, Blowfish.MODE_ECB)
    return cifrar.encrypt(pad(texto_plano.encode('utf-8'), Blowfish.block_size))

def texto_descifrado(texto_cifrado, llave):
    cifrar = Blowfish.new(llave, Blowfish.MODE_ECB)
    return unpad(cifrar.decrypt(texto_cifrado), Blowfish.block_size).decode('utf-8')

def contar_caracteres(texto):
    texto_sin_espacios = str(texto).replace(" ", "")
    return len(texto_sin_espacios)

def contar_caracteres2(texto):
    return len(texto)

def main():
    tiempo_inicio = time.time()
    documento = '10.txt'

    if not os.path.exists(documento):
        print(f"\nEl archivo {documento} no se encuentra. Cambie el nombre del archivo o verifique la ruta.")
        return None
    
    else:

        texto_plano = leer_txt(documento)
        print(f'\nDocumento de: {documento.split(".")[0] } palabras')
        print(f'\nTiempo para leer el archivo: {(time.time() - tiempo_inicio)* 1000} milisegundos')

        tiempo_inicio = time.time()
        llave = generar_llave()
        print(f'\nClave generada: {llave}')
        print(f'Tiempo para generar la clave: {(time.time() - tiempo_inicio)* 1000} milisegundos')

        tiempo_inicio = time.time()
        txt_cifrado = texto_cifrado(texto_plano, llave)
        #print(f'\nTexto cifrado: {txt_cifrado}')
        print(f'Tiempo para cifrar el texto: {(time.time() - tiempo_inicio)* 1000} milisegundos')

        tiempo_inicio = time.time()
        txt_descifrado = texto_descifrado(txt_cifrado, llave)
        #print(f'\nTexto descifrado: {txt_descifrado}')
        print(f'Tiempo para descifrar el texto: {(time.time() - tiempo_inicio)* 1000} milisegundos')

        caracter_entrada = contar_caracteres(texto_plano)
        print(f'\nCaracteres en el archivo: {caracter_entrada}')

        caracter_salida = contar_caracteres2(txt_cifrado)
        print(f'\nCaracteres en el archivo cifrado: {caracter_salida}\n')

if __name__ == '__main__':
    main()