matriz = [[0]*3 for _ in range(4)]

# print(matriz)

M = len(matriz)
N = len(matriz[0])

for i in range(M):
    for j in range(N):
        matriz[i][j] = int(input("Iingrese un numero: "))

for i in range(M):
    for j in range(N):
        print(f"{matriz[i][j]:5}", end = " " )
    print("")