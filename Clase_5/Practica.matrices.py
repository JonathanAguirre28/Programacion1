'''
Alumno: Jonathan Adrian Aguirre
Ejercicio matrices.

Un cuadrado mágico es una matriz cuadrada en la que la suma de los números en cada fila, cada columna y cada diagonal principal es la misma. Esto se conoce como constante mágica del cuadrado.
La misma se calcula: 
M = n*(n2 + 1)/2
Formalmente, un cuadrado mágico de orden n, es una matriz cuadrada de nxn donde los números enteros del 1 al n2  están dispuestos de tal manera que la suma de los números en cada fila, cada columna y cada diagonal principal es igual a la misma constante mágica.
Deberán desarrollar un programa que determine si el cuadrado de valores ingresado por el usuario es o no un cuadrado mágico. Tener en cuenta todas las validaciones posibles.
'''

matriz = [[0] * 3 for _ in range(3)]
M = len(matriz)#fila
N = len(matriz[0])#columna

constante_magica = M = N*(N** + 1)/2

for i in range(M):
    for j in range(N):
        while True:
            entrada = input(f"Ingresar un número para la posición ({i+1}, {j+1}): ")
            if entrada.isdigit():
                matriz[i][j] = int(entrada)
                break
            else:
                print("Error: Por favor, ingresar un número válido.")

for i in range(M):
    for j in range(N):
        print(f"{matriz[i][j]:6}", end=" ")
    print("")
    

