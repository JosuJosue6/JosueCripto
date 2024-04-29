#Algoritmo que realice el cifrado de una cadena de caracteres mediante 
#un método de sustitución Polialfabético de Vigenère. 
#La cadena se ingresa al iniciar el algoritmo. 
#El algoritmo debe mostrar la cadena de caracteres ingresada, la clave de 
#cifrado y la cadena de caracteres cifrada.

# Solicitar al usuario que ingrese la cadena de caracteres y la clave de cifrado
cadena = input("Ingrese la cadena de caracteres: ")
clave = input("Ingrese la clave de cifrado: ")

# Definir el alfabeto
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

# Crear una función para cifrar un carácter utilizando el método de Vigenère
def cifrar_caracter(caracter, clave):
    if caracter in alfabeto:
        indice = (alfabeto.index(caracter) + alfabeto.index(clave)) % len(alfabeto)
        return alfabeto[indice]
    else:
        return caracter

# Cifrar la cadena de caracteres utilizando la clave de cifrado y la función de cifrado
resultado = ''.join(cifrar_caracter(caracter, clave[i % len(clave)]) for i, caracter in enumerate(cadena.lower()))

# Imprimir la cadena de caracteres ingresada, la clave de cifrado y la cadena de caracteres cifrada
print("Cadena de caracteres ingresada:", cadena)
print("Clave de cifrado:", clave)
print("Cadena de caracteres cifrada:", resultado)