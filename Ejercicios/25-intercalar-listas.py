"""
2. Intercalar listas
Dadas dos listas de igual longitud, [1, 3, 5] y [2, 4, 6], 
crea una nueva lista intercalando sus elementos.
Resultado esperado: [1, 2, 3, 4, 5, 6].
"""
lista_01 = [1,3,5]
lista_02 = [2,4,6]
lista_new = []
longitud = len(lista_01)
numero = 0
for i in range(longitud):
    lista_new.append(lista_01[i])
    lista_new.append(lista_02[i])
           

print(lista_new)