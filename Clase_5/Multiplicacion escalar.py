matriz = [
    [4,7,9,4],
    [7,900,8,0],
    [1,900,3,5],
    [4,3,7,6]
]

escalar = 10

matriz_producto = [[0] * len(matriz[0]) for _ in range(len(matriz))]

for i in range(len(matriz_producto)):
    for j in range(len(matriz_producto[0])):
        matriz_producto[i][j] = matriz[i][j] * escalar
        
for i in range(len(matriz_producto)): # FILAS
    for j in range(len(matriz_producto[0])): # COLUMNAS
        print(f"{matriz_producto[i][j]:5}", end = " ")
    print("")