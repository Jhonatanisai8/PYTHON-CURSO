"""
Crea un programa que simule un sistema de inicio de sesión. Pide al usuario un nombre de usuario y contraseña. Si el nombre de usuario es "admin" y la contraseña es "1234", imprime "Acceso concedido". De lo contrario, imprime "Acceso denegado".
"""
usuario = "admin"
password = "1234"

usuario_ingresado = "admin"
password_ingresado = "1234"

if usuario == usuario_ingresado and password == password_ingresado:
    print("Acceso concedido.")
else:
    print("Acceso Denegado.")
    
