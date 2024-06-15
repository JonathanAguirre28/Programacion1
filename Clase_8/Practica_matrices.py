'''
Alumno: Aguirre Jonathan Adrian
Comision: 311
Turno: Noche

Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
Menú:
1. Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
2. Mostrar la recaudación de cada coche y línea.
3. Calcular y mostrar recaudación por línea.
4. Calcular y mostrar recaudación por coche.
5. Calcular y mostrar la recaudación total.
6. Salir
Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.

'''
from os import system
from Package_matrices.Generales import *
from Package_matrices.Especificas import *

matriz_recaudacion = [["Colectivos",1, 2, 3, 4, 5],
                      ["Lineas 1 :", 0, 0, 0, 0, 0],
                      ["Lineas 2 :", 0, 0, 0, 0, 0],
                      ["Lineas 3 :", 0, 0, 0, 0, 0]]

# #Matriz para testear el ejercicio
# matriz_recaudacion = [["Colectivos",1, 2, 3, 4, 5],
#                       ["Linea 1 ", 1, 2, 3, 5, 10],
#                       ["Linea 2 ", 6, 1, 4, 1, 10],
#                       ["Linea 3 ", 5, 1, 1, 5, 10]]
matriz_legajos = [[0] * 3 for _ in range(5)]
# #Bandera para probar con la matriz para testear
# bandera_ingreso = True
bandera_ingreso = False
bandera_seguir = True
while bandera_seguir == True:
    opcion = int(input("Bienvenido a la empreza de colecctivos, ingrese 1 para comenzar. Acontinuacion te dejo una lista con opciones: \n1.Cargar planilla\n2.Mostrar la recaudación de cada coche y línea\n3.Calcular y mostrar recaudación por línea\n4.Calcular y mostrar recaudación por coche\n5.Calcular y mostrar la recaudación total\n6.Salir.\n Elija una opcion: "))
    match opcion:
        case 1:
            bandera_ingreso = True
            cargar_legajos(matriz_legajos)
            legajo = int(input("Ingre su numero de legajo: "))
            if verificar_legajos(legajo, matriz_legajos):
                cargar_recaudacion(matriz_recaudacion)
            else:
                print("Error el legajo no exite!!!")
        case 2:
            if bandera_ingreso == True: 
                mostrar_recaudacion(matriz_recaudacion)
            else:
                print("Ingrese a la opcion 1")
        case 3:
            if bandera_ingreso == True:
                calcular_recaudacion_linea(matriz_recaudacion)
            else:
                print("Ingrese a la opcion 1")
        case 4:
            if bandera_ingreso == True:
                calcular_recaudacion_colectivo(matriz_recaudacion)
            else:
                print("Ingrese a la opcion 1")
        case 5:
            if bandera_ingreso == True:
                calcular_recaudacion_total(matriz_recaudacion)
            else:
                print("Ingrese a la opcion 1")
        case 6:
            print("Saliendo del programa")
            bandera_seguir = False
            
    system("pause")      
    system("cls")