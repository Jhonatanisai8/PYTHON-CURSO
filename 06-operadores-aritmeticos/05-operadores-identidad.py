print("OPERADORES IDENTIDAD")

"""
Los operadores de identidad en Python se utilizan para 
comparar si dos variables hacen referencia al mismo 
objeto en memoria.

is: Devuelve True si ambos operandos hacen referencia 
al mismo objeto.

is not: Devuelve True si ambos operandos no hacen 
referencia al mismo objeto.
"""

nombre = "Jhon Doe"
pelicula = "Jhon Doe"

son_lo_mismo = nombre is pelicula
print(son_lo_mismo)

alumno = "Richard"
son_distintos = alumno is not "Richard"
print(son_distintos)

