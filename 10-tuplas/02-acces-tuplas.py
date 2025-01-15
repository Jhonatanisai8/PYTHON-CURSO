
thistuple = ("apple", "banana", "cherry", "apple", "cherry")

# accdemos a un elemento por su indice
print(thistuple[1])

# accedemos al ultimo elemento
print(thistuple[-1])

# rango de indices
print(thistuple[1:4])

# desde el 0 al 4 
print(thistuple[:4])

# desde el 2 al ultimo 
print(thistuple[2:])

thistuple_02 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple_02[-4:-1])

# chekear si un item existe 
if "apple" in thistuple_02:
    print("Si 'apple' si esta en la tupla")