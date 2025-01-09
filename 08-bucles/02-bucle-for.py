"""
Un bucle for se utiliza para iterar 
sobre una secuencia (es decir, 
una lista, una tupla, un diccionario,
un conjunto o una cadena).
"""

# EJEMPLO
# Imprima cada fruta en una lista de frutas:
frutas = ["manzana","banana","fresa"]
for x in frutas:
    print(x)
    
    
# Recorre las letras de la palabra "pera":
for i in "pera":
    print(i)
    
# La declaración break => podemos detener un bucle
paises = ["colombia","venezuela","argentina"]
for pais in paises:
    print(pais)
# Cierra el bucle cuando pais es "venezuela"
    if pais == "venezuela":
        break
    
# La declaracion Continue => detener la iteracion actual y continuar 
marca_celulares = ["Samsung","Apple","Huawei"]
for celular in  marca_celulares:
    # no mostrara "Apple"
    if celular == "Apple":
        continue
    print(celular)