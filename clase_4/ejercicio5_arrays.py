'''
Alumno: Jonathan Adrian Aguirre
Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.
'''
def calcular_posicion_maximo_valor(lista: list) -> int:
    bandera = False
    maximo_valor = lista[0]
    for i in range(len(lista)):
        if  bandera == True or lista[i] > maximo_valor:
            maximo_valor = lista[i]
            posicion = i
            bandera
    resultado = print(f"El valor maximo es: {maximo_valor} y se encuentra en la posicion: {posicion}")
    return resultado
        
lista = [10,30,50,9,-10,100]
print(calcular_posicion_maximo_valor(lista))