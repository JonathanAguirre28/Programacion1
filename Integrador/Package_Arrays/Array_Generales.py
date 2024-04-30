def mostrar_suma_numeros_pares(mi_lista: list):
    acumulador_pares = 0
    for i in range(len(mi_lista)):
        if mi_lista[i] % 2 == 0:
            acumulador_pares += mi_lista[i]
    print("La suma de numeros pares es:", acumulador_pares)
    
def listar_numeros_impares(mi_lista: list):
    for i in range(len(mi_lista)):
        if i % 2 != 0:
            print("Número en posición impar:", mi_lista[i])
            
def listar_numeros_pares(mi_lista: list):
    for i in range(len(mi_lista)):
        if mi_lista[i] % 2 == 0:
            print("Los numeros pares son: ", mi_lista[i])
            
def listar_numeros_ingresados(mi_lista: list):      
    for i in range(len(mi_lista)):
        print("Los numeros ingresados son: ", mi_lista[i])
        