'''
Alumno: Jonathan Adrian Aguirre
Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.
'''
def reemplazar_nombres(lista: list, nombre: str, remplazo: str):
    contador_remplazo = 0
    for i in range (len(lista)):
        if lista[i] == nombre:
            lista[i] = remplazo
            contador_remplazo+=1
    return contador_remplazo          

lista = ["Jonathan", "Simon", "Juan", "Rocio"]
resultado = reemplazar_nombres(lista, "Jonathan", "Juan")
print(resultado)