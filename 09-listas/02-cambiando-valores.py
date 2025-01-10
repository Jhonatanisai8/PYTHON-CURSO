print("Cambiando valores en listas")

thislist =["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)

thislist[1] = "limon" #modifica el valor que esta en el indice 1
print(thislist)

thislist[1:3] = ["blackcurrant", "watermelon"] #cambiando el valor del indice 1 y 2
print(thislist)


paises_list = ["peru", "colombia", "venezuela"]
print(paises_list)
paises_list[1:2] = ["brazil", "ee.uu"] # inserta un nuevo valor
print(paises_list)

my_tecnologies = ["java","python","react"]
print(my_tecnologies)
my_tecnologies[1:3]  = ["c++"]
print(my_tecnologies)

# usando el metodo insert 
my_tecnologies.insert(0,"Jaja EE")
print(my_tecnologies)


