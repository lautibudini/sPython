#Implementa un programa que solicite al usuario que ingrese una lista de números.
#Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
#Nota: utilice la sentencia break cuando haga falta.
lista =[]
cant = int(input("ingrese la cantidad de numeros que quiere en su lista: "))
for i in range(cant):
    num = int(input("ingrese un numero:"))
    lista.append(num)
for num in lista:
    if (num <0):
        break
    print(num)

