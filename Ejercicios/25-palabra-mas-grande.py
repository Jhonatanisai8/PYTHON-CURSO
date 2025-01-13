"""
. Palabras más largas
Dada una lista de palabras, encuentra la palabra
más larga y su longitud.
Ejemplo: Para ["sol", "computadora", "mar"],
la palabra más larga es "computadora" con longitud 11.
"""

lista = ["sol", "computadora", "mar"]
mas_larga = list[0]
longi = len(lista)
for i in range(longi-1):
    if(len(lista[i]) > len(lista[i+1]) ):
        longi = lista[i]
print(longi)


