'''
Alumno: Jonathan Adrian Aguirre
comision: 311
Turno: noche
Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ej:
cadena = “murcielaguito”
“a” : 1
“e” : 1
“i” : 2
“o” : 1
“u” : 2
'''

def buscar_vocales(cadena: str, vocales: list) -> list:
    for i in range(len(vocales)):
        for j in range(len(cadena)):
            if vocales[i][0] == cadena [j]:
                vocales[i][1] += 1
    return vocales

def mostrar_contador_vocales(vocales: list):
    for i in range(len(vocales)):
        for j in range(len(vocales[0])):
            print(f"{vocales[i][j]:2}", end = "")
        print("")

cadena = "programacion"
vocales = [["a",0],
           ["e",0],
           ["i",0],
           ["o",0],
           ["u",0]]

buscar_vocales(cadena, vocales)
mostrar_contador_vocales(vocales)