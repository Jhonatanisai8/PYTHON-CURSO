"""
Pide tres números al usuario y determina cuál es el mayor, cuál el menor y si alguno de ellos es igual.
"""

numero_01= 34
numero_02 = 22
numero_03 = 34

if numero_01 > numero_02 and numero_01 > numero_03:
    print("El numero mayor es ",numero_01)
elif numero_02 > numero_01 and numero_02 > numero_03:
    print("El numero mayor es ",numero_02)
elif numero_03 > numero_01 and numero_03 > numero_02:
    print("El numero mayor es ",numero_03)
elif numero_01 == numero_02 and numero_01 == numero_03:
    print("El numero ",numero_01, " es igual a los demas")
elif numero_02 == numero_01 and numero_02 == numero_03:
    print("El numero ",numero_02, " es igual a los demas")
elif numero_03 == numero_01 and numero_03 == numero_02:
    print("El numero ",numero_03, " es igual a los demas")
    
    
    
    
    
