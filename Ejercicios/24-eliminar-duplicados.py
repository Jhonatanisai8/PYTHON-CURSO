"""
Eliminar duplicados
Dada la lista [1, 2, 2, 3, 4, 4, 5], elimina los elementos duplicados y crea una lista con valores únicos.
Imprime la nueva lista.
"""

lista = [1, 2, 2, 3, 4, 4, 5]
lista_nueva = []

for i in range(len(lista)):
    if lista[i] != lista[len(lista)-1-i]:
        lista_nueva.append(lista[i])
print(lista_nueva)