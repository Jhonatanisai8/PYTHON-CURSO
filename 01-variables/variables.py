# variables 
# es un contenedor para almacenar valores de datos 
# consejos 
# => puede empezar con una letra o un guin bajo 
# => no puede empezar con un numero
# => solo pueden tener caracteres alfanumericos y guiones bajos(A-z,0-9,_)
# => caseSensitive (no solo al comienzo sino en general)
# => no se pueden utilizar palabras reservadas de Python

x = 4

mi_nombre = "franco"

eres_mayor_edad = True

precio_producto = 12.2

_mi_edad = 12

mi_otra_variable = """
esto es un texto largo 
"""
mi_otra_variable_02 = '''
esto es un texto largo 02
'''

# le damos otro valor a la variable X
print(x)
x = "hola python"
print(mi_otra_variable)
print(mi_otra_variable_02)
print(_mi_edad)
print(mi_nombre)
print(eres_mayor_edad)
print(precio_producto)
print(x)

# CONVENCIONES DE ESCRITURA DE VARIABLES 
# CAMEL CASE
camelCase = "comienza y cada palabra siguiente comenzara con mayuscula"
# PASCAL CASE
PascalCase = "comienza con mayuscula y cada palabra siguiente comenzara con mayuscula"
# SNAKE CASE 
snake_case = "Se usan palabras en minuscula y las palabras son separadas con guiones bajos"

# muti asignacion 
x,y,z = 3,4,5
print(x)
print(y)
print(z)

a=b=c = "Hola Mundo desde Python"
print(a)
print(b)
print(c)



# coleccion de datos 
frutas = ["lima","mango","pera","papaya","palta"]
lima,mango,pera,papaya,palta = frutas
print(lima)
print(mango)
print(pera)
print(papaya)
print(palta)

# uso de print y salidas 
hola = "hola"
que_tal = "que tal"
print(hola+que_tal) #estamos concatenando

# variables GLOBALES o variables DE SCOPE
mi_variable_global = "mi variable global"

def funcion():
    # solo se usara en esta funcion
    mi_variable_scope = "variable de scope"




