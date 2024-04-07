"""
Actividad Extra
Creación de un programa básico de gestión de inventario.
Desarrollar un programa en Python que permita gestionar un inventario simple de
productos, incluyendo funciones básicas como agregar productos, eliminar productos y
mostrar el inventario.
El programa debe tener un menú interactivo que permita al usuario seleccionar las
siguientes operaciones:

-Agregar un nuevo producto al inventario, solicitando al usuario el nombre y la cantidad
inicial del producto.

-Eliminar un producto existente del inventario, solicitando al usuario el nombre del
producto a eliminar.

-Mostrar el inventario actual, que incluya el nombre y la cantidad de cada producto.

-Salir del programa

El inventario puede ser almacenado utilizando un diccionario simple, donde las claves sean
los nombres de los productos y los valores sean las cantidades.
Se deben manejar situaciones simples como la introducción de productos duplicados o la
eliminación de productos inexistentes"""

inventario = {}

def agregar_product():
    clave = input(" ingrese el nombre del procuto")
    valor = int(input("ingrese la cantidad actual del producto"))
    if clave in inventario:
        inventario[clave] = valor 
        print(" se actualizo la cantidad del producto ya existente.")
    else:
        inventario[clave] = valor 

def eliminar_product():
    clave = input("ingres el nombre del producto a eliminar : ")
    if clave in inventario:
        del inventario[clave]
    else: 
        print("el producto no existe.") 

def mostrar_inventari():
    for clave in inventario:
        print(f" {clave} : {inventario[clave]}")


#main

num = 0
while (num != 4):
    print (""" Bienvenido al menu de Gestion de Inventario , ingrese : 
       1- Para agregar un nuevo producto al inventario
       2- Para eliminar un producto existente del inventario
       3- Para mostrar el inventario actual
       4- Para salir del menu  """)
    num = int(input())

    match num:
        case 1:
            agregar_product()
        case 2:
            eliminar_product()
        case 3:
            mostrar_inventari()
        case 4:
            print("el menu finalizo")
        case _:
            print("el numero no es valido")
