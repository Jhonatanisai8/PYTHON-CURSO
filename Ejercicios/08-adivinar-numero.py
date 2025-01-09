"""
Adivina el Número
Crea un programa que genere un número aleatorio 
entre 1 y 20. Pide al usuario que adivine el 
número. Continúa el bucle hasta que el usuario
acierte.

Da pistas como "Es mayor" o "Es menor".
"""

import random 

numero_generado = random.randint(1,20)
print(numero_generado)
numero_ingresado = 0

while True:
    numero_ingresado = int(input("Ingresa un número por favor: "))
    if numero_ingresado < numero_generado:
        print("El numero debe ser mayor.")
    elif numero_ingresado > numero_generado:
        print("El numero debe ser menor.")
    else: 
        print("felicitaciones has adivinado el número.")
    if numero_generado == numero_ingresado:
        break
        
