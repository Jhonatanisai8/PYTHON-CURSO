print("El en Bucle For")
"""
La palabra clave else en un bucle 
for especifica un bloque de código
que se ejecutará cuando finalice 
el bucle.
"""

# ejemplo
for x in range(6):
    print(x)
else: 
    print("Finalizo el bucle.")
    
# ejemplo con la sentencia break 
for i in range(6):
    if i == 3: break
    print(i)
else:
    print("termino el bucle.")