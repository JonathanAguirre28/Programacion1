'''
Alumno: Jonathan Adrian Aguirre.
Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.
'''

def calcular_promedio_lista(lista: list):
    suma = 0
    for i in range (len(lista)):
        suma += lista[i]   
    promedio = suma / len(lista)
    return promedio

lista =  [10,9,8,7,6,-5,-4]
promedio = calcular_promedio_lista(lista)
print(promedio)
