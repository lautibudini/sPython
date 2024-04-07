#Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una
#con los número pares y otras con los que son impares. Imprima las listas al terminar de
#procesarlas.
lista =[]
neg = []
pos = []
cant = int(input("ingrese la cantidad de numeros que quiere en su lista: "))
for i in range(cant):
    num = int(input("ingrese un numero:"))
    lista.append(num)
for num in lista:
    if (num <0):
        neg.append(num)
    else:
        pos.append(num)
for i in pos:
    print(i)
for i in neg:
    print(i)
