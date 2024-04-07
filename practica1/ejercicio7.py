#Escribe un programa que tome una lista de números enteros como entrada del usuario.
#Luego, convierte cada número en la lista a string y únelos en una sola cadena,
#separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo
#de 3 de la cadena final.
list = []
while True:
    num = int(input("ingrese un numero entero"))
    if (num > 0):
        list.append(num)
    else:
        break
cadena = ""
for i in list:
    if (i % 3 != 0):
        cadena += str(f"{i}-")
print(cadena)
