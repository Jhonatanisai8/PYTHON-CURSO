"""
Menú Interactivo
Crea un programa con un menú que se repita hasta que el usuario 
seleccione la opción de salir. El menú puede incluir opciones como:

1: Saludar.
2: Mostrar la hora actual.
3: Salir.
Usa el bucle while para mantener el menú en funcionamiento.

"""
import datetime

hora_actual = datetime.datetime.now().time()

mensaje = """
MENU INTERACTIVO
1: Saludar.
2: Mostrar la hora actual.
3: Salir.

"""
while True:
    opcion = int(input(mensaje))
    if opcion == 1:
        print("Hola")
    elif opcion == 2:
        print(f"Hora Acual: {hora_actual}")
    elif opcion == 3:
        break
    else:
        print("Elige una opcion valida.!")