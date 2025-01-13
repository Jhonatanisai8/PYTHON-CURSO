"""
7. Reemplazar elementos
Dada una lista de números [5, 3, 8, 3, 2] y 
un número x, reemplaza todas las apariciones 
de x por otro número y.
Ejemplo: Si x = 3 y y = 7, el resultado debe 
ser [5, 7, 8, 7, 2].
"""

lista = [5, 3, 8, 3, 2]
print(lista)
lon = len(lista)

x = 2
y = 7

for i in range(lon):
    if lista[i] == x:
        lista[i] = y
print(lista)