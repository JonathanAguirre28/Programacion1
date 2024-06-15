# matriz = [
#     [4,7,9],
#     [7,9,8],
#     [1,5,3],
#     [4,3,7]
# ]
# rango M 4x3
# for i in range(4):
#     for j in range(3):
#         print(f"{i}--{j}")
#i recorre fila
#j reccorre columna
#print(matriz[2][1]) imprimo el numero 5
# M = len(matriz)
# N = len(matriz[0])
# for i in range(M): # FILAS
#     for j in range(N): # COLUMNAS
#         print(f"{matriz[i][j]}", end = " ")
#     print("")

matriz = [[0]*3 for _ in range(3)]


def ingrear_matriz(matriz: int):
    M = len(matriz)
    N = len(matriz[0])
    for i in range(M):
        for j in range(N):
            matriz[i][j] = int(input("Iingrese un numero: "))
ingrear_matriz(matriz)