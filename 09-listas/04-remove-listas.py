print("ELIMINANDO ELEMENTOS DE LA LISTA")

my_fruis = ["apple", "banana", "cherry"]
print(my_fruis)
my_fruis.remove("apple")
print(my_fruis)

my_fruis0_2 = ["apple", "banana", "cherry", "banana", "kiwi"]
print(my_fruis0_2)
my_fruis0_2.remove("banana") # elimina la primera coincidencia
print(my_fruis0_2)

# especificando un indice 
marcas_laptops = ["HP","Lenovo","Dell"]
print(marcas_laptops)
marcas_laptops.pop(0)
print(marcas_laptops)
marcas_laptops.pop() #elimina el ultimo
print(marcas_laptops)

# sentencia del
frutas = ["apple", "banana", "cherry"]
print(frutas)
del frutas[0]
print(frutas)
# del frutas
# print(frutas)

# limpiar toda la lista
frutas_lista = ["apple", "banana", "cherry"]
print(frutas_lista) 
frutas_lista.clear()
print(frutas_lista) 


