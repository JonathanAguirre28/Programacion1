def ingresar_numero_entero():
    while True:
        numero = input("Ingrese un número entero: ")
        if numero.lstrip('-').isdigit():
            return int(numero)
        else:
            print(f"Error: {numero} no es un numero entero, por favor, ingrese un número entero")

print("El número ingresado es:", ingresar_numero_entero())