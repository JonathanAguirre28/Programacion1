from Empleados import *
from Package_Validaciones.funciones import *
from os import system

lista_empleado = []
lista_empleado_eliminado = []

bandera_ingreso = False

def mostrar_menu():
    opcion = input("MENU\n1. Cargar\n2. Modificar\n3. Eliminar\n4. Mostrar todos los empleados\n5. Calcular el promedio de todos los salarios\n6. Ordenar \n7. Mostrar empleados eliminados \n8. Salir \nElija un opcion: ")
    return opcion
##################################################################################

system("cls")
while True:
    opcion = mostrar_menu()
    match opcion:
        case "1":
            ingresar_empleado_lista(lista_empleado)
            bandera_ingreso = True
        case "2":
            if bandera_ingreso == True:
                id = get_int("Ingrese el id: ", "Error id incorrecto")
                modificar_empleado(lista_empleado, id)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case "3":
            if bandera_ingreso == True:
                id = get_int("Ingrese el id: ", "Error id incorrecto")
                empleado_eliminado = eliminar_empleado(lista_empleado, id)
                if empleado_eliminado != None:
                    lista_empleado_eliminado.append(empleado_eliminado)
                    mostrar_empleado_con_id(empleado_eliminado)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case "4":
            if bandera_ingreso == True:
                mostrar_todos_los_empleados(lista_empleado)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case "5":
            if bandera_ingreso == True:
                mostrar_promedio_salarios(lista_empleado)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case "6":
            if bandera_ingreso == True:
                ordenar(lista_empleado)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case "7":
            if bandera_ingreso == True:
                if len(lista_empleado_eliminado) > 0:
                    mostrar_todos_los_empleados(lista_empleado_eliminado)
                else:
                    print("No hay empleados eliminados")
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case "8":
            break
            
    system("pause")
    system("cls")
    
