"""
Cuenta Regresiva
Pide al usuario que ingrese un número positivo. 
Utiliza un bucle while para realizar una cuenta 
regresiva desde ese número hasta 0, imprimiendo cada número.
"""

while True:
    numero = int(input("Ingresa un numero: "))
    if numero <= 0:
        print("Por favor el numero debe ser positivo.")
        continue
    while numero >= 0:
        print(f"contador {numero}")
        numero -= 1
    
    
    
        
    