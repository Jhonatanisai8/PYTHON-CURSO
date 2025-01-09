"""
Suma Acumulativa
Pide al usuario que ingrese números uno por uno. 
Detén el bucle cuando el usuario ingrese un número 
negativo y muestra la suma total de los números 
ingresados (excluyendo el negativo).
"""

suma = 0
while True:
    numero =int(input("Ingresa un numero: "))
    if numero < 0:
        break
    suma += numero
print("suma ",suma)