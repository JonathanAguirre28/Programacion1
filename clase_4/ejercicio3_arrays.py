'''
Alumno: Jonathan Adrian Aguirre.
Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.
'''

def calcular_producto(lista: list):
    multiplicacion = 1
    for i in range(len(lista)):
        multiplicacion *= lista[i]
    return multiplicacion

lista = [10,5,15]
resultado = calcular_producto(lista)
print(resultado)