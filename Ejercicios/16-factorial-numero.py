"""
Factorial de un Número
Pide al usuario un número entero
positivo y calcula su factorial 
utilizando un bucle for.
"""

numero = 5
factorial = 1
for x in range(1,numero+1):
    factorial *= x
print(f"Factorial de {numero} es {factorial}")