"""
6. Generar una matriz
Crea una matriz (lista de listas) de tamaño 3x3
con números consecutivos del 1 al 9.
Ejemplo: [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
"""
contador = 1
liista_new = []
for x in range(3):
    fila = []
    for j in range(3):
        fila.append(contador)
        contador += 1
    liista_new.append(fila)
lista = [[1,2,3],[4,5,6],[7,8,9]]
print(liista_new)