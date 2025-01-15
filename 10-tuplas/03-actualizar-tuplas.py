my_tuple = ("apple","banana","cherry")
print(my_tuple)
auxiliar = list(my_tuple)
auxiliar[1] = "kiwi"

my_tuple = tuple[auxiliar]

print(my_tuple)

vehiculos = ("avion","auto","tren","camion")
print(vehiculos)
auxiliar_vehiculos = list(vehiculos)
auxiliar_vehiculos.append("autobus")
vehiculos = tuple(auxiliar_vehiculos)

print(vehiculos)