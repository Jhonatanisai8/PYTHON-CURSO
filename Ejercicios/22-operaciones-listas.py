"""
4. Operaciones con listas
Dada la lista [1, 2, 3, 4, 5], multiplica cada 
elemento por 2 y crea una nueva lista con los resultados.
Imprime la lista original y la lista resultante.
"""

lista = [1, 2, 3, 4, 5]
lista_nueva = []
for x in  lista:
    lista_nueva.append(x * 2)
print(lista_nueva)