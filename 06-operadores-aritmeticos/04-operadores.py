print("HOLA MUNDO")

"""
Principales operadores lógicos en Python:

and: Devuelve True si ambas expresiones son True.
or: Devuelve True si al menos una de las expresiones es True.
not: Invierte el valor booleano de una expresión.
"""

edad = 17
tramite = edad >= 18 and edad <= 65
print(tramite) #false

semaforo = "rojo"
cruzar_semaforo = semaforo == "rojo" or semaforo == "amarillo" #true
print(cruzar_semaforo)


verdad = True

print(not verdad) #false
