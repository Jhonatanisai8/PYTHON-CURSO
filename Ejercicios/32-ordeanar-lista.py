"""
9. Ordenar lista sin usar métodos internos
Implementa una función que ordene una lista de
números [4, 2, 5, 1, 3] de menor a mayor sin 
usar funciones predefinidas como sort() o sorted().
"""

lista = [4, 2, 5, 1, 3]
lista_new = []  

while lista:  
    menor = lista[0]   
    for x in lista:    
        if x < menor:  
            menor = x  
    lista.remove(menor) 
    lista_new.append(menor)  

print("Lista original después de ordenarla:", lista_new)
