'''FUNCIONES_7 
Alumno: Jonathan Adrian Aguirre.
Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande '''


def encontrar_maximo_numero(numero_uno, numero_dos, numero_tres):
    if numero_uno > numero_dos and numero_uno > numero_tres:
        numero_maximo = numero_uno
    elif numero_dos > numero_tres:
        numero_maximo = numero_dos
    else:
        numero_maximo = numero_tres
        
    return numero_maximo
    
print("El numero maximo es: ", encontrar_maximo_numero(20,80,15))