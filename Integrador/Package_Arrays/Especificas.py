def mostrar_cantidad_numeros_positivos(mi_lista: list):
    cantidad_positivos = 0
    for i in range (len(mi_lista)):
        if mi_lista[i] > 0:
            cantidad_positivos += 1
    print("La cantidad de numeros positivos es:", cantidad_positivos)
        
def mostrar_cantidad_numeros_negativos(mi_lista: list):
    cantidad_negativos = 0
    for i in range (len(mi_lista)):
        if mi_lista[i] < 0:
            cantidad_negativos += 1
    print("La cantidad de numeros negativos es:", cantidad_negativos)
    
def mostrar_maximo_valor_impar(mi_lista: list):
    contador_impar = 0
    maximo_valor = None 
    for i in range(len(mi_lista)):
        if mi_lista[i] % 2 != 0:
            contador_impar += 1
            if contador_impar == 1 or mi_lista[i] > maximo_valor:
                maximo_valor = mi_lista[i]

    if maximo_valor != None:  
        print("El maximo valor impar es:", maximo_valor)
    else:
        print("No se ingresaron numeros impares")

