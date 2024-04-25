'''FUNCIONES_1
Alumno: Jonathan Adrian Aguirre.
Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.'''

#def ingresar_numero_entero():
    #numero = input("Ingrese un número entero: ")
    #return int(numero)  

#print("El numero ingresado es: ", ingresar_numero_entero())

def get_int(mensaje: str, minimo: int, maximo: int) -> int:
    numero = input(mensaje)
    numero = int(numero)
    while numero < minimo or numero > maximo:
        numero = input(f"Error!! {mensaje}")
        numero = int(numero)
    return numero
#numero_ingresado = get_int()
#print(f"El numero ingresado es: {numero_ingresado}")

edad = get_int("Ingrese su edad: ", 15, 30) # la edad va entre 15 - 30
    
legajo = get_int("Ingrese su legajo: ", 1500, 2756) # El legajo va entre 1500- 2756


nota = get_int("Ingrese su nota: ", 1, 10) # La nota va entre 1 - 10
