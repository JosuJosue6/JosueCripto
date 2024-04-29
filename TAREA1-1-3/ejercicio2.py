#Algoritmo que realice el cifrado de un mensaje por permutación de filas, 
#teniendo como clave n filas. 
#Tanto n como el texto del mensaje se ingresan al iniciar el algoritmo. 
#El algoritmo debe controlar que el número de caracteres del 
#mensaje (sin espacios), sea menor o igual que n x n. 
#Imprima la matriz de cifrado, el mensaje original y el mensaje cifrado. 
#Si en la matriz de cifrado sobran espacios para almacenar los caracteres 
#Perdel mensaje original, estos deben llenarse con "*".

import numpy as np

# Solicitar al usuario que ingrese el número de filas y el mensaje
n = int(input("Ingrese el número de filas: "))
mensaje = input("Ingrese el mensaje: ")

# Eliminar los espacios del mensaje
mensaje = mensaje.replace(" ", "")

# Comprobar si el número de caracteres del mensaje es menor o igual a n x n
if len(mensaje) > n*n:
    print("El mensaje es demasiado largo para la clave proporcionada.")
else:
    # Crear una matriz de cifrado de tamaño n x n
    matriz = np.full((n, n), "*")

    # Llenar la matriz con el mensaje, fila por fila
    for i in range(n):
        for j in range(n):
            if i*n + j < len(mensaje):
                matriz[i, j] = mensaje[i*n + j]

    # Imprimir la matriz de cifrado, el mensaje original y el mensaje cifrado
    print("Matriz de cifrado:")
    print(matriz)
    print("Mensaje original:", mensaje)
    print("Mensaje cifrado:", "".join(matriz.flatten(order='F')))
