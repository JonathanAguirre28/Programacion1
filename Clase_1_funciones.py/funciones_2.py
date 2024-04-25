'''FUNCIONES_2 
Alumno: Jonathan Adrian Aguirre.
Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.'''

def ingresar_numero_flotante():
    numero = input("Ingrese un numero flotante: ")
    return float(numero)

print("El numero ingresado es: ", ingresar_numero_flotante())