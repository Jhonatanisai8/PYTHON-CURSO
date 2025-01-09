"""Promedio de Números
Pide al usuario que ingrese números uno por uno.
Calcula y muestra el promedio de los números 
ingresados cuando el usuario ingrese un número
negativo.
"""
suma = 0
total_elementos = 0
while True:
    numero = int(input("Ingresa un numero: "))
    if numero < 0:
        break;
    total_elementos += 1
    suma += numero
    promedio = suma / total_elementos
    
    
print(f"""
      Suma: {suma}
      Total elementos: {total_elementos}
      Promedio: {promedio}
      """)

    