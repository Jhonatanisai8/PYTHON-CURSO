"""
6. Filtrar números pares
Crea una lista de números del 1 al 20.
Usa una comprensión de listas para filtrar solo los números pares.
"""

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

lista_nueva = [x for x in lista if x %2 == 0]
print(lista_nueva)