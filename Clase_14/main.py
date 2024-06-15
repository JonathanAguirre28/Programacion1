# lista = [
#     {'dni': 3, 'nombre': 'Pepe', 'apellido': 'Gomez', 'nota': 10},
#     {'dni': 4, 'nombre': 'Pepe', 'apellido': 'Gomez', 'nota': 9},
#     {'dni': 2, 'nombre': 'Pepe', 'apellido': 'Gomez', 'nota': 7}
# ]

# # ingresar_alumno_lista(lista)
# # ingresar_alumno_lista(lista)

# mostrar_un_alumno(lista[1])

# mostrar_todos_los_alumnos(lista)

from Alumno import *
from os import system

def mostrar_menu():
    opcion = input("MENU\n1. Cargar\n2. Modificar\n3. Eliminar\n4. Mostrar\n5. Salir\nElija un opcion: ")
    return opcion
##################################################################################
lista_alumno = [
    {'dni': 32145267, 'nombre': 'Pepe', 'apellido': 'Gomez', 'nota': 10},
    {'dni': 43545687, 'nombre': 'Pepe', 'apellido': 'Gomez', 'nota': 9},
    {'dni': 22545454, 'nombre': 'Pepe', 'apellido': 'Gomez', 'nota': 7}
]

system("cls")
while True:
    opcion = mostrar_menu()
    match opcion:
        case "1":
            ingresar_alumno_lista(lista_alumno)
        case "2":
            dni = int(input("Ingrese el dni: "))
            modificar_alumnos(lista_alumno, dni)
        case "3":
            dni = int(input("Ingrese el dni: "))
            eliminar_alumno(lista_alumno, dni)
        case "4":
            mostrar_todos_los_alumnos(lista_alumno)
        case "5":
            break
    system("pause")
    system("cls")


