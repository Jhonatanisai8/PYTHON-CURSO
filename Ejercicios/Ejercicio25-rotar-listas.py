"""
1. Rotar elementos de una lista
Dada una lista [1, 2, 3, 4, 5] y un número n, rota 
los elementos de la lista n posiciones hacia la derecha.
Ejemplo: Si n = 2, 
la lista resultante debe ser [4, 5, 1, 2, 3]
"""

lista = [1,2,3,4,5]
longitud = len(lista)
print(longitud)
print("")
lista_nueva = []
n = 1
for i in range (longitud):
    numero = lista[(i+n+1)%longitud]
    lista_nueva.append(numero)

print(lista_nueva)