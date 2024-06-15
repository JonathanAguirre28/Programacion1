#Funcion para mostrar reacudacion de cada colectivo y linea
def mostrar_recaudacion(matriz_recaudacion: list):
    for i in range(len(matriz_recaudacion)):
        for j in range(len(matriz_recaudacion[0])):
            print(f"{matriz_recaudacion[i][j]:5}", end = "")
        print("")
    return matriz_recaudacion

#Funcion para calcular y mostrar recaudacion por linea
def calcular_recaudacion_linea(matriz_recaudacion: list):
    for i in range(1, len(matriz_recaudacion)):
        recaudacion_x_linea = 0
        for j in range(1, len(matriz_recaudacion[0])):
            recaudacion_x_linea += matriz_recaudacion[i][j]
        print(f"La recaudacion total de la {matriz_recaudacion[i][0]} es: ${recaudacion_x_linea}")
        
#Funcion para calcular y mostrar recaudacion por colectivo
def calcular_recaudacion_colectivo(matriz_recaudacion: list):
    for j in range(1, len(matriz_recaudacion[0])):
        recaudacion_x_colectivos = 0
        for i in range(1, len(matriz_recaudacion)):
            recaudacion_x_colectivos += matriz_recaudacion[i][j]
        print(f"La recaudacion del colectivo {matriz_recaudacion[0][j]} es: ${recaudacion_x_colectivos}")



#Funcion para calcular y mostrar recaudacion total
def calcular_recaudacion_total(matriz_recaudacion: list):
    recaudacion_total = 0
    for i in range(1, len(matriz_recaudacion)):
        for j in range(1, len(matriz_recaudacion[0])):
            recaudacion_total += matriz_recaudacion[i][j]
            
    return print(f"La suma de recaudacion total es: ${recaudacion_total}")