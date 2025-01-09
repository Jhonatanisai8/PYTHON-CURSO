"""
Invertir un String
Pide al usuario una palabra 
y utiliza un bucle for para imprimirla al revés.
"""

cadena = "hola"

for i in range(len(cadena)):
    print(cadena[len(cadena)-1-i])