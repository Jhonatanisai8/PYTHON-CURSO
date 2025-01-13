"""
Ej8. Lista al cuadrado
Dada una lista de números [2, 4, 6, 8],
crea una nueva lista con los cuadrados de cada elemento.
Resultado esperado: [4, 16, 36, 64].
"""

lista = [2, 4, 6, 8]
print(lista)
for x in range(len(lista)):
    lista[x] = lista[x] * lista[x]
print(lista)

