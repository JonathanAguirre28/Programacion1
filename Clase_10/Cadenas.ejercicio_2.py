'''
Alumno: Jonathan Adrian Aguirre
comision: 311
Turno: noche
Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.
'''
def buscar_incidencia(cadena: str, caracter: str):
    incidencia = -1
    for i in range(len(cadena)):
        if caracter == cadena[i]:
            incidencia = i
            break
            
    return incidencia

cadena = "se estan complicando los ejercicios"
caracter = "a"
resultado = buscar_incidencia(cadena, caracter)
print(resultado)

