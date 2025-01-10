print("Listas")

my_lista = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
paises = list(["peru","colombia"])
print(my_lista)
print(paises)

print(f"Tamaño de la lista: {len(my_lista)}")
print(f"Valor en el indice 0 {my_lista[0]}")
print(f"Valor en el indice ultimo {my_lista[-1]}")
print(f"Valor en el indice 2 al 5 {my_lista[2:5]}")
print(f"Valor en el indice 0 al 4 {my_lista[:4]}")
print(f"Valor en el indice -4 al 1 {my_lista[-4:-1]}")

# verificar si un valor esta dentro de la lista 

if "mango" in my_lista:
    print("Mango si esta en la lista")