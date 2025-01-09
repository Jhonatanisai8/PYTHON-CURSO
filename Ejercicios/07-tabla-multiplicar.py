"""
Tabla de Multiplicar
Pide al usuario un número y utiliza un bucle
while para imprimir la tabla de multiplicar 
de ese número (del 1 al 10).
"""
contador = 1
while True:
    numero = int(input("Ingresa un numero: "))    
    contador = 0
    while contador <= 10:
        print(f"{numero} X {contador} = {contador * numero}")
        contador += 1
    if numero < 0:
        break
    