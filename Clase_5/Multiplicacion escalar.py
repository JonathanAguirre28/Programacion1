matriz_a = [
    [4,7,9,4],
    [7,900,8,0],
    [1,900,3,5],
    [4,3,7,6]
]

matriz_b = [
    [4,7,9,4],
    [7,900,8,0],
    [1,900,3,5],
    [4,3,7,6]
]

escalar = -6

matriz_suma = [[0] * len(matriz_a[0])  for _ in range(len(matriz_a))]  

for j in range(len(matriz_suma)): #columnas
    for i in range(len(matriz_suma[0])): #filas
        matriz_suma[i][j] = matriz_a[i][j] + matriz_b[i][j]
        
for j in range(len(matriz_suma)): #columnas
    for i in range(len(matriz_suma[0])): #filas
        print(f"{matriz_suma[i][j]:5}", end = " ")
    print("")