print("UNION DE LISTAS ")
lista_01 = ["uno","dos","tres"]
lista_02 = [1,2,3,]

lista_03 = lista_01 + lista_02
print(lista_03)

lista_03.clear()

lista_02.extend(lista_01)
print(lista_02)
