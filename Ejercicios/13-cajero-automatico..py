"""
Cajero Automático Simulado
Crea un programa que simule un cajero automático:

Muestra un saldo inicial de $1000.
Ofrece opciones para depositar, retirar o salir.
Usa un bucle while para permitir varias operaciones 
hasta que el usuario decida salir.
"""

saldo_inicial = 1000
mensaje = """
MENU INTERACTIVO
1: Depositar.
2: Retirar
3: Salir.

"""
print(f"Saldo Actual: {saldo_inicial}")
while True:
    opcion = int(input(mensaje))
    if opcion == 1:
        saldo_deposito = int(input("Monto a depositar: "))
        saldo_inicial += saldo_deposito
        print("Depositando.....")
        print(f"Saldo Actual: {saldo_inicial}")
    elif opcion == 2:
        saldo_retirar = int(input("Monto a retirar: "))
        saldo_inicial -= saldo_retirar
        print("Depositando.....")
        print(f"Saldo Actual: {saldo_inicial}")
    elif opcion == 3:
        break
    else:
        print("Elige una opcion valida.!")