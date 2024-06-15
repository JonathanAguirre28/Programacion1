'''
Alumno: Jonathan Adrian Aguirre
Comision: 311
Turno: Noche


Enunciado:

La empresa "Recursos Inhumanos" nos ha solicitado desarrollar un software de gestión de empleados para llevar a cabo un control exhaustivo de los mismos.

Datos correspondientes a cada empleado:
ID
Nombre
Apellido
DNI
Puesto
Salario

Consideraciones:

El programa deberá gestionar una lista de hasta 20 empleados. Cada empleado será representado mediante un diccionario.
Si se alcanza el límite de 20 empleados, se deberá notificar al usuario. Solo se podrá ingresar un empleado en caso de que se efectúe una vacante nueva (o sea que se elimine uno).
Al ingresar un empleado, el ID debe ser autoincremental, comenzando en 1. Cada empleado tendrá un ID único.
El resto de los datos deberán ser ingresados por consola.

Validaciones:

Nombre y Apellido: Deben contener solo caracteres alfabéticos, ser nombres propios y no exceder los 20 caracteres. No pueden contener números ni caracteres especiales.
Salario: Debe ser un valor numérico entero no menor a $234315.
Puesto: Debe ser uno de los siguientes: “Gerente” / “Supervisor” / “Analista” / “Encargado” / “Asistente”.
DNI: Debe ser un valor numérico entre 5000000 y 99999999.

Opciones del menú:

Ingresar empleado: Pedirá los datos necesarios y dará de alta a un nuevo empleado, asignando un ID autoincremental.
Modificar empleado: Permitirá alterar cualquier dato del empleado excepto su ID. Se usará el ID para identificar al empleado a modificar. Se mostrará un submenú para seleccionar qué datos modificar. Indicando si se realizaron modificaciones o no.
Eliminar empleado: Eliminará permanentemente a un empleado de la lista original. Se pedirá el ID del empleado a eliminar. 
Mostrar todos: Imprimirá por consola la información de todos los empleados en formato de tabla:

***************************************************************
|    Nombre    |   Apellido   |      Puesto      |   Salario  |
—-------------------------------------------------------------
|    German    |  Scarafilo   |     Gerente      |  $500.000  |
|   Giovanni   |  Lucchetta   |    Supervisor    |  $300.000  |
***************************************************************

Calcular salario promedio: Calculará e imprimirá el salario promedio de todos los empleados.
Buscar empleado por DNI: Permitir al usuario buscar y mostrar la información de un empleado específico ingresando su DNI.
Ordenar empleados: Ofrecer la opción de ordenar y mostrar la lista de empleados por nombre, apellido, o salario de forma ascendente o descendente.
Salir: Terminará la ejecución del programa.

Requisitos adicionales:

El programa deberá estar correctamente modularizado, haciendo uso de módulos, paquetes y funciones propias para solicitar enteros, flotantes y cadenas, así como para las validaciones de cada uno de estos tipos de datos.
El código debe estar programado de manera eficiente y siguiendo buenas prácticas de la programación y las reglas de estilo de la cátedra.
'''

from Package_Validaciones.funciones import *
from Package_Validaciones.ordenamiento import *
from os import system

def crear_empleado(id: int, nombre: str, apellido: str, dni: int, puesto: str, salario: int) -> dict:
    diccionario_empleado = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "puesto": puesto,
        "salario": salario,
    }
    return diccionario_empleado

def ingresar_empleado_lista(lista_empleado: list) -> dict:
    system("cls")
    if buscar_disponibilidad_empleado(lista_empleado):    
        id = get_int("Ingrese el id: ", "Error id incorrecto")
        nombre = ingrese_una_cadena_de_texto("Ingrese el nombre: ", "Error nombre incorrecto")
        apellido = ingrese_una_cadena_de_texto("Ingrese el apellido: ", "Error apellido incorrecto")
        dni = get_int_dni("Ingrese el DNI: ", "Error dni incorrecto")
        puesto = ingrese_el_puesto("Ingrese el puesto (Gerente-Supervisor-Analista-Encargado-Asistente): ", "Error puesto incorrecto")
        salario = get_int_salario("Ingrese el salario: ", "Error, no ingresaste un numero entero o no el numero ingresado es menor a $234315")
        
        diccionario_empleado = crear_empleado(id, nombre, apellido, dni, puesto, salario)
        
        lista_empleado.append(diccionario_empleado)
    else:
        print("No se pueden ingresar mas de 20 empleados elimine uno.")


# def buscar_empleado(lista_empleado: list[dict], id: int) -> dict:
#     for empleado in lista_empleado:
#         if id == empleado["id"]:
#             return empleado
#         else:
#             print("Empleado no encontrado")
        
    
def buscar_disponibilidad_empleado(lista_empleados: list[dict]) -> int | None:
    
    disponibilidad = False
    if len(lista_empleados) < 20:
        disponibilidad = True
    return disponibilidad
    
######################################################################################

def mostrar_un_empleado(un_empleado: dict):
    print(f"{un_empleado["nombre"]:>15}{un_empleado["apellido"]:>19}{un_empleado["dni"]:>22}{un_empleado["puesto"]:>23}{un_empleado["salario"]:>20}\n")   
    
def mostrar_todos_los_empleados(lista_empleado: list[dict]):
    print("""
    ********************************************************************************************************
    |     Nombre      |     Apellido      |        DNI         |      Puesto       |        Salario        |
    -------------------------------------------------------------------------------------------------------- """)
    for empleado in lista_empleado:
        if len(lista_empleado) > 0:
            mostrar_un_empleado(empleado)
        else:
            print("No hay empleados en la lista")
        
#######################################################################################

def modificar_empleado(lista_empleado: list[dict], id: int):
    system("cls")
    for empleado in lista_empleado:
        if id == empleado["id"]:
            mostrar_empleado_con_id(empleado)
            opcion = input("Empleado encontrado, Ingrese que desea modificar\n1. Modificar nombre\n2. Modificar Apellido\n3. Modificar DNI\n4. Modificar puesto\n5. Modificar Salario\n6. salir\n Elija una opcion: ")
            match opcion:
                case "1":
                    nuevo_nombre = ingrese_una_cadena_de_texto("Ingrese el nuevo nombre: ", "Error nombre incorrecto")
                    empleado["nombre"] = nuevo_nombre
                    break
                case "2":
                    nuevo_apellido = ingrese_una_cadena_de_texto("Ingrese el nuevo apellido: ", "Error apellido incorrecto")
                    empleado["apellido"] = nuevo_apellido
                    break
                case "3":
                    nuevo_dni = get_int_dni("Ingrese el nuevo dni: ", "Error dni incorrecto")
                    empleado["dni"] = nuevo_dni
                case "4":
                    nuevo_puesto = ingrese_el_puesto("Ingrese el nuevo puesto: ", "Error puesto incorrecto")
                    empleado["puesto"] = nuevo_puesto
                    break
                case "5":
                    nuevo_salario = get_int_salario("Ingrese el nuevo salario: ", "Error salario incorrecto o menor a $234315")
                    empleado["salario"] = nuevo_salario
                    break
                case "6":
                    break
        else:
            print("No hay empleados con ese numero de id")

def eliminar_empleado(lista_empleado: list[dict], id: int):
    system("cls")
    eliminado = None
    for empleado in lista_empleado:
        if id == empleado["id"]:
            eliminado = empleado
            break
        else:
            print("Id no existente")
    if eliminado != None:
        lista_empleado.remove(eliminado)
        print("Empleado eliminado: ")
    return eliminado

def mostrar_empleado_con_id(un_empleado: dict):
    print("""
    **********************************************************************************************************************
    |     id      |     Nombre      |     Apellido      |        DNI         |      Puesto       |        Salario        |
    ---------------------------------------------------------------------------------------------------------------------- """)
    print(f"{un_empleado["id"]:>12}{un_empleado["nombre"]:>18}{un_empleado["apellido"]:>19}{un_empleado["dni"]:>21}{un_empleado["puesto"]:>22}{un_empleado["salario"]:>20}\n")  
    


def mostrar_promedio_salarios(lista_empleado: list[dict]):
    suma_salario = 0
    for empleado in lista_empleado:
        suma_salario += empleado["salario"]
    if len(lista_empleado) > 0:
        promedio = suma_salario / len(lista_empleado)
    else:
        promedio = 0
    print(f"El promedio de los salarios es: ${round(promedio)}")    
    
    
def ordenar(lista_empleados: list[dict]):
    system("cls")
    opcion = input("Ordenar por: \n1. Nombre\n2. Apellido\n3. Salario\nIngresar opcion: ")
    orden = input("¿Como desea ordenar?\n1. Ascendente\n2. Descendente\nIngresar opcion: ")
    match opcion:
        case "1":
            if orden == "1":
                ordenar_por_nombre_ascendente(lista_empleados)
            else:
                ordenar_por_nombre_descendente(lista_empleados)
        case "2":
            if orden == "1":
                ordenar_por_apellido_ascendente(lista_empleados)
            else:
                ordenar_por_apellido_descendente(lista_empleados)
        case "3":
            if orden == "1":
                ordenar_salario_mayor_a_menor(lista_empleados)
            else:
                ordenar_salario_menor_a_mayor(lista_empleados)