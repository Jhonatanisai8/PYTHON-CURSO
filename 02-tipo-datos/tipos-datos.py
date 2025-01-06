print("Tipos de datos")

# string (srt)
cadena = "hola"
texto = 'hola'
print(type(cadena))
print(type(texto))

# enteros (int)
edad = 12
print(type(edad))

# decimal (float)
precio = 12.3
print(type(precio))

# numeros complejos (complex)
numero_complejo = 5 + 2j
print(type(numero_complejo))

# listas ordenada mutable (list)
lista = ["hola",12,23.4]
print(type(lista))

# tuplas coleccion ordenada inmutable (tuple)
mi_tupla = (1,"sas",34)
print(type(mi_tupla))

#rangos  (range)
rango = range(1,10)
print(type(rango))

# diccionarios (dict)
mi_diccionario = {
    "nombre":"dani",
    "edad":12,
    "ciudad" : {
        "id": 1,
        "nombre":"ciudad 1"
    }
}
print(type(mi_diccionario))

# conjuntos colecion desordenada de elemetos unicos y mutables (set)
mi_conjunto = {1,1,2,2,3}
print(type(mi_conjunto))

# fronzenSet([]) coleccion desordenada de elementos unicos e inmutables  (frozenset)
conjunto_inmutable = frozenset([1,1,23,4])
print(type(conjunto_inmutable))

# boleanos (bool)
mayor_edad = True
print(type(mayor_edad))