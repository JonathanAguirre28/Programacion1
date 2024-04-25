'''FUNCIONES_5 
Alumno: Jonathan Adrian Aguirre.
Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área'''

import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

radio = float(input("Ingrese la longitud del radio del círculo: "))
area = calcular_area_circulo(radio)
print("El área del círculo es:", area)
