"""Tabla de Multiplicar
Pide al usuario un número y utiliza un bucle 
for para imprimir la tabla de multiplicar de 
ese número (del 1 al 10)."""

numero = 3

for x in range(1,11):
    print(f"{numero} X {x} = {x*numero} ")