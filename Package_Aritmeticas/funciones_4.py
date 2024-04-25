'''FUNCIONES_4 
Alumno: Jonathan Adrian Aguirre.
Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.'''

def ingresar_numero_entero():
    while True:
        numero = input("Ingrese un número entero: ")
        if numero.lstrip('-').isdigit():
            return int(numero)
        else:
            print(f"Error: {numero} no es un numero entero, por favor, ingrese un número entero")

print("El número ingresado es:", ingresar_numero_entero())


def ingresar_numero_flotante():
    while True:
        numero = input("Ingrese un número flotante: ")
        if '.' in numero.replace("-", "", 1) and numero.replace(".", "", 1).isdigit():
            return float(numero)
        else:
            print("Error: Por favor, ingrese un número flotante")

print("El número ingresado es:", ingresar_numero_flotante())




def ingrese_una_cadena_de_texto():
    while True:
        cadena = input("Ingrese una cadena: ")
        if cadena.isalpha():
            return str(cadena)
        else:
            print(f"Error {cadena} no es un cadena de texto, reingrese: ")

print("La cadena es: ", ingrese_una_cadena_de_texto())