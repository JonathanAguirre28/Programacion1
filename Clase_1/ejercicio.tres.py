#Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
#Alumno: Jonathan Adrian Aguirre



def mostrar_numero_par_impar(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
    
numero = input("Ingrese un numero")
numero = int(numero)
mostrar_numero_par_impar(numero)

