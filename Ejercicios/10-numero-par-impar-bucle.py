"""Número Par o Impar
Pide al usuario que ingrese números. Para cada número, 
indica si es par o impar. Detén el programa cuando el 
usuario ingrese un 0.
"""

while True:
    numero = int(input("Ingresa un número: "))    
    if numero < 0: 
        break
    if numero % 2 == 0:
        print(f"El numero {numero} es par.")
    else:
        print(f"El numero {numero} es impar.")
        
