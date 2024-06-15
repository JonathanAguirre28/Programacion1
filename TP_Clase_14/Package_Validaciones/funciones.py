def get_int(mensaje: str, mensaje_error: str):
    while True:
        numero = input(mensaje)
        if numero.lstrip('-').isdigit():
            return int(numero)
        else:
            print(mensaje_error)


def ingresar_numero_flotante():
    while True:
        numero = input("Ingrese un número flotante: ")
        if '.' in numero.replace("-", "", 1) and numero.replace(".", "", 1).isdigit():
            return float(numero)
        else:
            print("Error: Por favor, ingrese un número flotante")


def ingrese_una_cadena_de_texto(mensaje: str, mensaje_error: str):
    while True:
        cadena = input(mensaje)
        if cadena.isalpha() and len(cadena) <= 20:
            return str(cadena)
        else:
            print(mensaje_error)
            
def get_int_salario(mensaje: str, mensaje_error: str):
    while True:
        numero = input(mensaje)
        if numero.lstrip('-').isdigit() and int(numero) > 234315:
            return int(numero)
        else:
            print(mensaje_error)

def ingrese_el_puesto(mensaje: str, mensaje_error: str):
    puestos = ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]
    while True:
        cadena = input(mensaje)
        if cadena.isalpha() and len(cadena) <= 20 and (cadena in puestos):
            return str(cadena)
        else:
            print(mensaje_error)
            
def get_int_dni(mensaje: str, mensaje_error: str):
    while True:
        numero = input(mensaje)
        if numero.lstrip('-').isdigit() and (int(numero) >= 5000000 and int(numero) <= 99999999):
            return int(numero)
        else:
            print(mensaje_error)
            
def confirmar_eliminar(lista: list, empleado: str):
    pass
    