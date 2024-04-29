# def sumar_todos_los_numeros(numero: int) -> int:
#     if numero > 0:
#         resultado = numero
#     else:
#         resto = numero % 10
#         resultado = resto // 10
#     return resto + sumar_todos_los_numeros(resultado)
# numero = sumar_todos_los_numeros(1234)
# print(numero)

def mostrar_suma_numeros_pares(mi_lista: list):
    acumulador_pares = 0
    for i in range(len(mi_lista)):
        if mi_lista[i] % 2 == 0:
            acumulador_pares += mi_lista[i]
    print("La suma de numeros pares es:", acumulador_pares)
    
mi_lista = [10,-10,9,-8,7,5,3,1]
    
mostrar_suma_numeros_pares(mi_lista)