"""
Ej. Encontrar los duplicados
Dada una lista, encuentra todos los elementos 
que aparecen más de una vez y cuántas veces se repiten.
Ejemplo: En [1, 2, 3, 2, 4, 1], los duplicados 
son 1 (2 veces) y 2 (2 veces).
"""

lista = [1, 2, 3, 2, 4, 1]
conteo = {}
for numero in lista:
    if numero in conteo: 
        conteo[numero] += 1
    else:
        conteo[numero] = 1
        
duplicados = []
for clave, valor in conteo.items():
    if valor > 1:
        duplicados.append((clave,valor))
        
print("Duplicados y sus repeticiones:", duplicados)

