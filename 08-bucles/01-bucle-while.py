print("BUCLES EN PYTHON")
"""
Bucle while: Se utiliza cuando no sabemos de antemano 
cuántas veces se ejecutará el código. La ejecución 
continúa mientras una condición se evalúe como 
verdadera.
while condicion:
  # Código a ejecutar mientras la condición sea verdadera
  
break: Permite salir de un bucle de forma anticipada.
continue: Salta a la siguiente iteración del bucle.
"""

iterador = 1 
while iterador <= 10:
    print("Hola ",iterador)
    iterador += 1
    
    # usando el break 
contador = 0
while contador <= 5:
    print("Contador ",contador)
    if contador == 2:
        break # Sale del bucle cuando contador es 2
    contador += 1
    
iteracion = 0
while iteracion <= 5:
    print("Contador ",iteracion)
    iteracion += 1
    if iteracion == 2:
        continue # Salta la iteracion 2 osea lo omite
    

# ejemplo con true

while True:
    resp = input("¿Desea continuar. (s/n))?: ")
    if resp == "n":
        break
    
    