#Algoritmo que realice el cifrado de una cadena de caracteres mediante 
#un método de sustitución Monoalfabético de desplazamiento n caracteres 
#a la derecha. Tanto la palabra como el valor de n se ingresan al iniciar 
#el algoritmo. El algoritmo debe mostrar el alfabeto original, el alfabeto 
#cifrado, la cadena de caracteres ingresada y su resultado.


# Solicitar al usuario que ingrese la cadena de caracteres y el valor de desplazamiento
cadena = input("Ingrese la cadena de caracteres: ")
n = int(input("Ingrese el valor de desplazamiento: "))

# Definir el alfabeto original
alfabeto_original = 'abcdefghijklmnopqrstuvwxyz'

# Crear el alfabeto cifrado desplazando el alfabeto original n caracteres a la derecha
alfabeto_cifrado = alfabeto_original[n:] + alfabeto_original[:n]

# Crear un diccionario de mapeo de cada carácter del alfabeto original a su correspondiente carácter en el alfabeto cifrado
mapeo = {original: cifrado for original, cifrado in zip(alfabeto_original, alfabeto_cifrado)}

# Cifrar la cadena de caracteres reemplazando cada carácter por su correspondiente en el alfabeto cifrado
resultado = ''.join(mapeo.get(caracter, caracter) for caracter in cadena.lower())

# Imprimir el alfabeto original, el alfabeto cifrado, la cadena de caracteres ingresada y su resultado
print("Alfabeto original:", alfabeto_original)
print("Alfabeto cifrado:", alfabeto_cifrado)
print("Cadena de caracteres ingresada:", cadena)
print("Resultado:", resultado)