def get_int(mensaje:str, mensaje_error: str, minimo: int, maximo:int) -> int|None:
    numero = input(mensaje)
    numero = int(numero)
    
    while numero < minimo or numero > maximo:
        numero = int(input(f"{mensaje_error}, {mensaje}"))
        numero = int(numero)

    return numero 

def pedir_numeros_enteros(mi_lista: list):
    for i in range(len(mi_lista)):
        mi_lista[i] = get_int("Ingrese un numero entero mayor a -1000 y menor a 1000: ", "Reingrese un numero", -1000, 1000)