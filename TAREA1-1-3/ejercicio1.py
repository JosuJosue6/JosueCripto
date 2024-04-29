import itertools

#Algoritmo que escriba todas las permutaciones 
#posibles de una palabra de longitud n SIN espacios 
#(Anagrama). La palabra se ingresa al iniciar el algoritmo. 
#El algoritmo debe mostrar el número total de permutaciones 
#y las 10 primeras ordenadas alfabéticamente.
palabra = input("Ingrese una palabra: ")
permutaciones = list(itertools.permutations(palabra))

print("Permutaciones totales:", len(permutaciones))
print("Primeras 10 permutaciones (ordenadas alfabeticamente):")
for perm in sorted(permutaciones)[:10]:
    print("".join(perm))