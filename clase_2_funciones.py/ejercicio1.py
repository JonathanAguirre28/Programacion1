'''
Funciones_2
Ejercicio N° 1.
Alumno: Jonathan Adrian Aguirre

1.
Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo: 
En donde:
mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
mínimo: valor mínimo admitido (inclusive)
máximo: valor máximo admitido (inclusive)
reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
'''


def get_int(mensaje:str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    contador_reintentos = 0
    numero = input(mensaje)
    numero = int(numero)
    
    while numero < minimo or numero > maximo and contador_reintentos < reintentos:
        contador_reintentos += 1
        numero = int(input(f"{mensaje_error} tiene {reintentos} reintentos, {mensaje}"))
        numero = int(numero)
        if reintentos -1 == contador_reintentos:
            return None

    return numero 

numero_int = get_int("Ingrese un numero entero mayor a 20 y menor a 40: ", "Error", 20, 40, 3)
print(numero_int)