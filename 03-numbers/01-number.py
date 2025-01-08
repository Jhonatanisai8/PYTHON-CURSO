# enteros (int)
edad = 12
print(edad)
print(type(edad))

# decimal (float)
precio = 12.3
print(precio)
print(type(precio))

# numeros complejos (complex)
numero_complejo = 5 + 2j
print(numero_complejo)
print(type(numero_complejo))

# casteo 
entero = 12
decimal = 23.2
complejo = 4 + 2j

entero_decimal = float(entero)
decimal_entero = int(decimal)
entero_complejo = complex(entero)
decimal_complejo = complex(decimal)

print("casteo")
print(entero_decimal)
print(decimal_entero)
print(entero_complejo)
print(decimal_complejo)
