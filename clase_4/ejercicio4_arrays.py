'''
Alumno: Jonathan Adrian Aguirre.
Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.
'''
def calcular_posicion_maximo_valor(lista: list) -> int:
    bandera = False
    maximo_valor = lista[0]
    for i in range(len(lista)):
        if  bandera == True or lista[i] > maximo_valor:
            maximo_valor = lista[i]
            posicion = i
            bandera 
    return posicion
        
lista = [10,30,50,9,-10,100]
resultado = calcular_posicion_maximo_valor(lista)
print(f"El valor maximo encontrado esta en la posicion: {resultado}")
