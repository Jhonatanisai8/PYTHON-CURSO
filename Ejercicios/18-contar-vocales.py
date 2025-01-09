"""
Contar Vocales
Pide al usuario que ingrese una frase y utiliza
un bucle for para contar cuántas vocales tiene.
"""

frase = "la vida es bella"
contador = 0
for letra in frase:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador += 1
print(f"La frase tiene {contador} vocales.")