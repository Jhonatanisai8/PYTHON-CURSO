print("Add List Items")

my_frutas = ["manzana","pera","mandarina"]
print(my_frutas)

# agrega el final de la lista
my_frutas.append("mango")
print(my_frutas)

# agrega en la posicion 0
my_frutas.insert(0,"naranja")
print(my_frutas)


# fusion de listas 
climas = ["caluroso","lluvioso","seco"]
paises = ["peru","argentina","chile"]
print(climas)
climas.extend(paises)
print(climas)

# fusion de listas y tuplas 
celulares = ["Samsung A51","Huawei P30 Pro","Motorola Edge50 Ultra"]
laptops = ("Hp","Lenovo")
celulares.extend(laptops)
print(celulares)