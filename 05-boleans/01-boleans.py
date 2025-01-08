"""
los booleanos (booleans) son un tipo de dato que solo puede tener uno de dos valores:

True (verdadero)
False (falso)

En Python, cualquier valor puede evaluarse como un booleano. La regla general es:

Los valores "vacíos" o "cero" se consideran False.
Los valores "no vacíos" o "distintos de cero" se consideran True.
"""

vedadero = True
falso = False

string = bool("h") #devuelce si esta vacio 
print(string)

numero= bool(2024)
print(numero)

lista = bool(["asa",2])
print(lista)

diccionario = bool({"sadas"})
print(diccionario)

nulo = bool(None)
print(nulo)