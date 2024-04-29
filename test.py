def cifrado_permutacion(mensaje, n):
    # Eliminar espacios y convertir a mayúsculas
    mensaje = mensaje.replace(" ", "").upper()
    
    # Verificar que el mensaje sea menor o igual a n*n
    if len(mensaje) > n*n:
        print("El mensaje es demasiado largo para la clave proporcionada.")
        return
    
    # Completar el mensaje con asteriscos si es necesario
    mensaje += "*" * (n*n - len(mensaje))
    
    # Crear la matriz de cifrado
    matriz_cifrado = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(mensaje[i*n + j])
        matriz_cifrado.append(fila)
    
    # Imprimir la matriz de cifrado
    print("Matriz de cifrado:")
    for fila in matriz_cifrado:
        print(fila)
    
    # Imprimir el mensaje original
    print("\nMensaje original:", mensaje[:n*n])
    
    # Imprimir el mensaje cifrado
    mensaje_cifrado = ""
    for j in range(n):
        for i in range(n):
            mensaje_cifrado += matriz_cifrado[i][j]
    print("Mensaje cifrado:", mensaje_cifrado)

# Ejemplo de uso
mensaje = input("Ingrese el mensaje a cifrar: ")
n = int(input("Ingrese el número de filas para la clave de cifrado: "))

cifrado_permutacion(mensaje, n)