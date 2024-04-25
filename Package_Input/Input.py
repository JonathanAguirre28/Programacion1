from Validate import *

def get_int(mensaje:str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) -> int|None:
    contador_reintentos = 0
    numero = input(mensaje)
    numero = int(numero)
    
    while numero < minimo or numero > maximo and contador_reintentos < reintentos:
        contador_reintentos += 1
        numero = int(input(f"{mensaje_error} tiene {reintentos} reintentos, {mensaje}"))
        numero = int(numero)
        if reintentos == contador_reintentos:
            return None

    return numero 

numero_int = get_int("Ingrese un numero entero mayor a 20 y menor a 40: ", "Reingrese un numero", 20, 40, 3)
print(numero_int)

def get_float(mensaje:str, mensaje_error: str, minimo: int, maximo:int, reintentos: float) -> float|None:
    contador_reintentos = 0
    numero = input(mensaje)
    numero = float(numero)
    
    while numero < minimo or numero > maximo and contador_reintentos < reintentos:
        contador_reintentos += 1
        numero = float(input(f"{mensaje_error} tiene {reintentos} reintentos, {mensaje}"))
        numero = float(numero)
        if reintentos == contador_reintentos:
            return None

    return numero 

numero_float = get_float("Ingrese un numero decimal mayor a 1.5 y menor a 5.5: ", "Reingrese un numero", 1.5, 5.5, 3)
print(numero_float)

def get_string(cadena: str, longitud: int) -> str|None:
    if len(cadena) == longitud:
        mensaje = "Exelente coincide"
    else:
        mensaje = "Error la cadena no conincide con la longitud"
        
    return mensaje
        
    
mensaje = get_string("programacion", 12)
print(mensaje)