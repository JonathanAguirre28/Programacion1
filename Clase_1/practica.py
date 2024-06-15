'''
Alumnos: Jonathan Adrian Aguirre _ Juan bencivengo_ Alegre yamila. 
Ejercicio matrices.
Comision: 311.
Turno: noche.
Un cuadrado mágico es una matriz cuadrada en la que la suma de los números en cada fila, cada columna y cada diagonal principal es la misma. Esto se conoce como constante mágica del cuadrado.
La misma se calcula: 
M = n*(n2 + 1)/2
Formalmente, un cuadrado mágico de orden n, es una matriz cuadrada de nxn donde los números enteros del 1 al n2  están dispuestos de tal manera que la suma de los números en cada fila, cada columna y cada diagonal principal es igual a la misma constante mágica.
Deberán desarrollar un programa que determine si el cuadrado de valores ingresado por el usuario es o no un cuadrado mágico. Tener en cuenta todas las validaciones posibles.
Link del video : https://drive.google.com/file/d/1txxqj_lEKlLEIBy4r0rf7oZ1VPn_V0zm/view?usp=drive_link
'''

matriz = [[0]*3 for _ in range(3)]


def ingrear_matriz(matriz: int):
    M = len(matriz)
    N = len(matriz[0])
    for i in range(M):
        for j in range(N):
            matriz[i][j] = int(input("Iingrese un numero: "))
            
    for i in range(len(matriz)): 
        for j in range(len(matriz[0])): 
            print(f"{matriz[i][j]:5}", end = " ")
        print("")
            
ingrear_matriz(matriz)

def calcular_cuadrado_magico(matriz: int):
    resultado = True
    n = len(matriz) 
    ecuacion = n * (n**2 + 1) / 2
    
    for fila in matriz:
        if len(fila) != n:
            resultado = True
            
    for i in range(n):
        suma_filas = 0
        suma_columnas = 0
        for j in range(len(matriz[0])):
            suma_filas += matriz[i][j]
            suma_columnas += matriz[j][i] 
            
        if suma_filas != ecuacion or suma_columnas != ecuacion:
            resultado = False   
    
    
    suma_diagonal_principal = 0
    suma_diagonal_secundaria = 0
    for i in range(n):
        suma_diagonal_principal += matriz[i][i]
        suma_diagonal_secundaria += matriz[i][n-1-i]
        
    if suma_diagonal_principal != ecuacion or suma_diagonal_secundaria != ecuacion:
        resultado = False
        
    return resultado

if calcular_cuadrado_magico(matriz):
    print("Es un cuadrado magico")
else:
    print("No es un cuadrado magico")

