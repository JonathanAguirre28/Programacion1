'''
Alumno: Jonathan Adrian Aguirre
Comision: 311
Turno: Noche

Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
1. Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
2. Mostrar la cantidad de números positivos y negativos.
3. Mostrar la sumatoria de los números pares.
4. Informar el mayor de los números impares.
5. Listar todos los números ingresados.
6 .Listar todos los números pares.
7. Listar los números de las posiciones impares.  
8. Salir

Notas:
Solo se podrá ingresar a las opciones 2 a 7, siempre y cuando el usuario haya ingresado los datos solicitados.

Todas las opciones deberán ser programadas en funciones: habrá funciones específicas (por ejemplo para determinar si un número es positivo o negativo) y funciones de nivel general (por ejemplo una función que liste los números pares). Tener en cuenta las características de la programación funcional.

Las funciones específicas deberán estar en el módulo “Especificas.py”, mientras que las generales en el módulo “Array_Generales.py”. Todos estos módulos deben estar integrados en el paquete Package_Arrays.
Utilizar las funciones input del paquete Package_Input.
Consejo: Primero realizar el desarrollo de las funciones y probarlas. Luego, armar los módulos y paquetes.
'''

from os import system
from Package_Arrays.Array_Generales import *
from Package_Arrays.Especificas import *
from Package_Input.input import *

bandera_ingreso = False
bandera_seguir = True
mi_lista = [0] * 10

while bandera_seguir == True:
    opcion = int(input("Bienvenido ingrese 1 para comenzar. Acontinuacion te dejo una lista con opciones: \n2.Mostrar la cantidad de numeros positivos y negativos\n3.Mostrar la sumatoria de los números pares\n4.Informar el mayor de los números impares\n5.Listar todos los números ingresados\n6.Listar todos los números pares\n7.Listar los números de las posiciones impares\nElija una opcion: "))
    match opcion:
        case 1:
            pedir_numeros_enteros(mi_lista)
            bandera_ingreso = True
        case 2:
            if bandera_ingreso == True:
                mostrar_cantidad_numeros_positivos(mi_lista)
                mostrar_cantidad_numeros_negativos(mi_lista)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case 3:
            if bandera_ingreso == True:
                mostrar_suma_numeros_pares(mi_lista)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case 4:
            if bandera_ingreso == True:
                mostrar_maximo_valor_impar(mi_lista)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case 5:
            if bandera_ingreso == True:
                listar_numeros_ingresados(mi_lista)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case 6:
            if bandera_ingreso == True:
                listar_numeros_pares(mi_lista)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case 7:
            if bandera_ingreso == True:
                listar_numeros_impares(mi_lista)
            else:
                print("No se ingresaron los valores. Ingrese a la opcion 1")
        case 8:
            bandera_ingreso = False
            
    system("pause")      
    system("cls")