"""
10. Eliminar extremos
Dada una lista de números, elimina el 
valor más alto y el más bajo.
Ejemplo: Para [10, 2, 8, 4, 6], la lista
resultante debe ser [8, 4, 6].
"""

lista =  [10, 2, 8, 4, 6]
print(lista)
mas_alto = max(lista)
mas_bajo = min(lista)

lista.remove(mas_alto)
lista.remove(mas_bajo)
print(lista)
