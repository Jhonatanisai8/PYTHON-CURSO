print("Strings en PYTHON")

texto = "hola mundo"
saludo = 'Hola'
bienvenida = """hola mundo desde python"""
ciudad = '''las vegas'''

# type
print(type(bienvenida))

# arrays de caracteres 
caracter = texto[0] #accedemos a un caracter por su indice
print(caracter)

lontigud = len(texto)
print(f"{texto} tiene {lontigud} caracteres")

print("hola" in texto) #devuelve True o False
print("hoLa" not in texto) #devuelve True o False

print(texto[0:5]) #cortamos una palabra desde un indice o otro


# modificadores de texto 
nombre = "flor"
print(nombre.lower())
print(nombre.upper())
print(nombre.capitalize()) # la primera letra en mayuscula

espacio_texto = "   hola "
print(espacio_texto.strip()) #elimina los espacios en blanco
print(espacio_texto.replace("hola","mundo")) #reemplaza

print("hola,mundo,que,tal".split(",")) #separa en una lista 



