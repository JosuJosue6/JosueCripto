#Algoritmo que realice el cifrado de una cadena de caracteres 
#utilizando la siguiente tabla de cifrado:
#La cadena de caracteres se ingresa al iniciar el programa. 
#Si algún caracter del texto no existe en la matriz, coloque "**". 
#Imprima la matriz de cifrado, el mensaje original y el mensaje cifrado.
# Solicitar al usuario que ingrese la cadena de caracteres
cadena = input("Ingrese la cadena de caracteres: ")

# Definir la matriz de cifrado
matriz_cifrado = {
    'A': 'a', 'S': 'b', 'D': 'c', 'F': 'd', 'G': 'e',
    'Q': 'f', 'W': 'g', 'E': 'h', 'R': 'i', 'T': 'j',
    'a': 'k', 's': 'l', 'd': 'm', 'f': 'n', 'g': 'o',
    'q': 'p', 'w': 'q', 'e': 'r', 'r': 's', 't': 't',
    'Z': 'u', 'X': 'v', 'C': 'x', 'V': 'y', 'B': 'z'
}

# Cifrar la cadena de caracteres reemplazando cada carácter por su correspondiente en la matriz de cifrado
resultado = ''.join(matriz_cifrado.get(caracter, '**') for caracter in cadena)

# Imprimir la matriz de cifrado, la cadena de caracteres ingresada y la cadena de caracteres cifrada
print("Matriz de cifrado:", matriz_cifrado)
print("Cadena de caracteres ingresada:", cadena)
print("Cadena de caracteres cifrada:", resultado)