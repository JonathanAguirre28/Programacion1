def ordenar_salario_menor_a_mayor(lista_empleado: list[dict]):
    for i in range (0, len(lista_empleado)-1):
        for j in range(i + 1, len(lista_empleado)):
            if lista_empleado[j]["salario"] < lista_empleado[i]["salario"]:
                auxiliar = lista_empleado[i]
                lista_empleado[i]= lista_empleado[j]
                lista_empleado[j] = auxiliar              

                
def ordenar_salario_mayor_a_menor(lista_empleado: list[dict]):
    for i in range (0, len(lista_empleado)-1):
        for j in range(i + 1, len(lista_empleado)):
            if lista_empleado[j]["salario"] > lista_empleado[i]["salario"]:
                auxiliar = lista_empleado[i]
                lista_empleado[i] = lista_empleado[j]
                lista_empleado[j] = auxiliar   
                
def ordenar_por_nombre_ascendente(lista_empleados: list[dict]):
    for i in range(0, len(lista_empleados)-1):
        for j in range(i + 1, len(lista_empleados)):
            if lista_empleados[i]["nombre"] > lista_empleados[j]["nombre"]:
                auxiliar = lista_empleados[i]["nombre"]
                lista_empleados[i]["nombre"] = lista_empleados[j]["nombre"] 
                lista_empleados[j]["nombre"] = auxiliar 
                
def ordenar_por_nombre_descendente(lista_empleados: list[dict]):
    for i in range(0, len(lista_empleados)-1):
        for j in range(i + 1, len(lista_empleados)):
            if lista_empleados[i]["nombre"] < lista_empleados[j]["nombre"]:
                auxiliar = lista_empleados[i]["nombre"]
                lista_empleados[i]["nombre"] = lista_empleados[j]["nombre"] 
                lista_empleados[j]["nombre"] = auxiliar

def ordenar_por_apellido_ascendente(lista_empleados: list[dict]):
    for i in range(0, len(lista_empleados)-1):
        for j in range(i + 1, len(lista_empleados)):
            if lista_empleados[i]["apellido"] > lista_empleados[j]["apellido"]:
                auxiliar = lista_empleados[i]["apellido"]
                lista_empleados[i]["apellido"] = lista_empleados[j]["apellido"] 
                lista_empleados[j]["apellido"] = auxiliar
                
def ordenar_por_apellido_descendente(lista_empleados: list[dict]):
    for i in range(0, len(lista_empleados)-1):
        for j in range(i + 1, len(lista_empleados)):
            if lista_empleados[i]["apellido"] < lista_empleados[j]["apellido"]:
                auxiliar = lista_empleados[i]["apellido"]
                lista_empleados[i]["apellido"] = lista_empleados[j]["apellido"] 
                lista_empleados[j]["apellido"] = auxiliar