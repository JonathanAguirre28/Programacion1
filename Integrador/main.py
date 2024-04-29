'''
Alumno: Jonathan Adrian Aguirre

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

bandera_ingreso = False
bandera_seguir = True
mi_lista = [0] * 10

def get_int(mensaje:str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    contador_reintentos = 0
    numero = input(mensaje)
    numero = int(numero)
    
    while numero < minimo or numero > maximo and contador_reintentos < reintentos:
        contador_reintentos += 1
        numero = int(input(f"{mensaje_error} tiene {reintentos} reintentos, {mensaje}"))
        numero = int(numero)
        if reintentos == contador_reintentos:
            return None

    return numero 

def pedir_numeros_enteros(mi_lista: list):
    for i in range(len(mi_lista)):
        mi_lista[i] = get_int("Ingrese un numero entero mayor a -1000 y menor a 1000: ", "Reingrese un numero", -1000, 1000, 10)

def mostrar_cantidad_numeros_positivos(mi_lista: list):
    cantidad_positivos = 0
    for i in range (len(mi_lista)):
        if mi_lista[i] > 0:
            cantidad_positivos += 1
    print("La cantidad de numeros positivos es:", cantidad_positivos)
        
def mostrar_cantidad_numeros_negativos(mi_lista: list):
    cantidad_negativos = 0
    for i in range (len(mi_lista)):
        if mi_lista[i] < 0:
            cantidad_negativos += 1
    print("La cantidad de numeros negativos es:", cantidad_negativos)
    
def mostrar_suma_numeros_pares(mi_lista: list):
    acumulador_pares = 0
    for i in range(len(mi_lista)):
        if mi_lista[i] % 2 == 0:
            acumulador_pares += mi_lista[i]
    print("La suma de numeros pares es:", acumulador_pares)

def mostrar_maximo_valor_impar(mi_lista: list):
    contador_impar = 0
    maximo_valor = None 
    for i in range(len(mi_lista)):
        if mi_lista[i] % 2 != 0:
            contador_impar += 1
            if contador_impar == 1 or mi_lista[i] > maximo_valor:
                maximo_valor = mi_lista[i]
    if maximo_valor != None:  
        print("El maximo valor impar es:", maximo_valor)
    else:
        print("No se ingresaron numeros impares")

def listar_numeros_ingresados(mi_lista: list):      
    for i in range(len(mi_lista)):
        print("Los numeros ingresados son: ", mi_lista[i])

def listar_numeros_pares(mi_lista: list):
    for i in range(len(mi_lista)):
        if mi_lista[i] % 2 == 0:
            print("Los numeros pares son: ", mi_lista[i])

def listar_numeros_impares(mi_lista: list):
    for i in range(len(mi_lista)):
        if mi_lista[i] & 2 != 0:
            print("Los numeros impares son: ", mi_lista[i])

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