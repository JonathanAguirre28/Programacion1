'''
Alumno: Jonathan Adrian Aguirre.
Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.
'''

def calcular_promedio_lista(lista: list):
    suma = 0
    for i in range (len(lista)):
        if len(lista) > 0:
            suma += lista[i]   
        promedio = suma / len(lista)
    return promedio

lista =  [10,9,8,7,6]
promedio = calcular_promedio_lista(lista)
print(promedio)