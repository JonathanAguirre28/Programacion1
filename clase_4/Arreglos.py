

def pedir_numeros_enteros():
    for i in range(len(mi_lista)):
        mi_lista[i] = int(input("Ingrese un numero: "))
mi_lista = [0] * 10
pedir_numeros_enteros()

def mostrar_numeros():      
    for i in range(len(mi_lista)):
        print(mi_lista[i])
mostrar_numeros()