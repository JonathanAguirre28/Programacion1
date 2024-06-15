'''
Alumno: Jonathan Adrian Aguirre
comision: 311
Turno: noche
Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.
'''
def determinar_palindromo(cadena: str) -> bool:
    palindromo = True
    for i in range(len(cadena)):
        if cadena[i] != cadena[-(i+1)]:
            palindromo = False
            break
    return palindromo

cadena = "aerea"
print(determinar_palindromo(cadena))