matriz = [
    [4,7,9],
    [7,900,8],
    [1,900,3],
    [4,3,7]
]

M = len(matriz)
N = len(matriz[0])

for j in range(N): #columnas
    for i in range(M): #filas
        print(f"{matriz[i][j]:5}", end = " ")
    print("")