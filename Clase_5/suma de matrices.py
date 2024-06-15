matriz_a = [
    [4,7,9,4],
    [7,900,8,0],
    [1,900,3,5],
    [4,3,7,6]
]

matriz_b = [
    [5,5,6,3],
    [1,50,6,1],
    [2,30,5,6],
    [6,4,5,7]
]

escalar = 10

matriz_suma = [[0] * len(matriz_a[0]) for _ in range(len(matriz_a))]

for i in range(len(matriz_suma)):
    for j in range(len(matriz_suma[0])):
        matriz_suma[i][j] = matriz_a[i][j] + matriz_b[i][j]
        
for i in range(len(matriz_suma)): # FILAS
    for j in range(len(matriz_suma[0])): # COLUMNAS
        print(f"{matriz_suma[i][j]:5}", end = " ")
    print("")