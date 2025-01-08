print("Operadores de pertenencia")
"""
Los operadores de pertenencia en Python se utilizan 
para verificar si un valor se encuentra dentro de 
una secuencia (como una cadena, lista, tupla o conjunto).

in: Devuelve True si el valor se encuentra dentro de 
la secuencia, y False en caso contrario.

not in: Es lo opuesto a in, devuelve True si el valor 
no se encuentra dentro de la secuencia.
"""

lista_frutas = ["Manzana","Pera","Mandarina","Fresa"]

esta_manzana_en_lista = "Manzana" in lista_frutas
print(esta_manzana_en_lista) #true

esta_papaya_en_lista = "Papaya" not in lista_frutas
print(esta_papaya_en_lista) #true

# cadenas
saludo = "Hola Mundo"
hola_en_saludo = "Hola" in saludo
print(hola_en_saludo) #true

que_tal_en_saludo = "Que tal" not in saludo
print(que_tal_en_saludo) #true

