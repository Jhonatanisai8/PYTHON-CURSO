"""
3. Suma y promedio
Crea una lista de números enteros [5, 10, 15, 20, 25].
Calcula la suma de los números y el promedio.
"""

lista = [1,2,3,4,5,6,7,8,9,10]

suma = 0
for x in lista:
    suma += x

print(f"suma total {suma}, promedio {suma/len(lista)}")