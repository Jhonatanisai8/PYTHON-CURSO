"""
5. Intersección de listas
Dadas dos listas [1, 2, 3, 4] y [3, 4, 5, 6], 
encuentra los elementos que están presentes 
en ambas listas.

Resultado esperado: [3, 4].
"""
lista_01 = [1,4,5,6,7,2,3,2,5,6] 
lista_02 = [9,8,6,4,7,3,1,9,0]

lista_duplicados = []

for x in lista_02:
    if x in lista_01:
        lista_duplicados.append(x)
            
print(lista_duplicados)
 
 
