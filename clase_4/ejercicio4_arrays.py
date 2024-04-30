'''
Alumno: Jonathan Adrian Aguirre.
Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
'''
def calcular_maximo_valor(lista: list) -> int:
    bandera = False
    maximo_valor = 0
    for i in range(len(lista)):
        if  bandera == True or lista[i] > maximo_valor:
            maximo_valor = lista[i]
            bandera
    return maximo_valor
        
lista = [10,30,50,9,-10]
resultado = calcular_maximo_valor(lista)
print(resultado)