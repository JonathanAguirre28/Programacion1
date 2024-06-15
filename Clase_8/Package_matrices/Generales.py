import random
#Funcion para crear matrices
def cargar_legajos(matriz_legajos: list):
    M = len(matriz_legajos)
    N = len(matriz_legajos[0])
    
    for i in range(M):
        for j in range(N):
            matriz_legajos[i][j] = random.randint(1000, 9999)            
            
    for i in range(M):
        for j in range(N):
            print(f"{matriz_legajos[i][j]:5}", end = " " )
        print("")
        
    return matriz_legajos

#Funcion para cargar recaudacion
def cargar_recaudacion(matriz_recaudacion: list):
    linea_colectivos = int(input("Ingrese una linea de colectivo del (1 al 3): "))
    while linea_colectivos > 3:
        linea_colectivos = int(input("Error reingrese una linea de colectivo del (1 al 3): "))
    colectivo = int(input("Ingrese el numero de colectivo del (1 al 5): "))
    while colectivo > 5:
        colectivo = int(input("Error reingrese el numeor del colectivo del (1 al 5): "))
    recaudacion = int(input("Ingrese la recaudacion: "))
    matriz_recaudacion[linea_colectivos][colectivo] += recaudacion
    return matriz_recaudacion

#Funcion verificar lelgajos
def verificar_legajos(legajo: int, matriz_legajos: list):
    verificacion_legajos = False
    for i in range(len(matriz_legajos)):
        for j in range(len(matriz_legajos[0])):
            if legajo == matriz_legajos[i][j]:
                verificacion_legajos = True
                continue

    return verificacion_legajos