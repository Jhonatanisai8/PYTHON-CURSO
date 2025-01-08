print("Metodos mas comunes de String")

cadena = "hOLA munDO"

cadena_minuscula = cadena.lower();
print(cadena_minuscula) 

candena_mayuscula = cadena.upper();
print(candena_mayuscula)

primera_letra_mayuscula = cadena.capitalize();
print(primera_letra_mayuscula)

primera_letra_palabras_mayus = cadena.title()
print(primera_letra_palabras_mayus)

espacios_eliminados_principio_final = cadena.strip()
print(espacios_eliminados_principio_final)

reemplazar_texto =cadena.replace("munDO","PYTHON")
print(reemplazar_texto)

borrar_espacios_principio = " hola".lstrip()
print(borrar_espacios_principio)

borrar_espacios_final = "hola ".rstrip()
print(borrar_espacios_final)

empieza_con = "hola java".startswith("hola")
print(empieza_con)

termina_con = "hola java".endswith("hola")
print(termina_con)

numero_veces = "Hola Hola Mundo".count("Hola")
print(numero_veces)

indice_donde_empieza = "Hola".find("Mundo")
print(indice_donde_empieza)

lista_cadena = cadena.split(" ")
print(lista_cadena)

cadena_generada = cadena.join(lista_cadena)
print(cadena_generada)

tupla_denerada = "Hola Mundo".partition(" ") 
print(tupla_denerada)

es_digito = "4".isdigit()
print(es_digito)

es_alfa = "asa#".isalpha()
print(es_alfa)

es_alfa_numerico = "ads233".isalnum()
print(es_alfa_numerico)

estan_en_miniscula = "asdasd".islower()
estan_en_mayuscula = "ADSF".isupper()
print(estan_en_miniscula)
print(estan_en_mayuscula)

