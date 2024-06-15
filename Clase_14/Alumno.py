# C 
def crear_alumno(dni: int, nombre: str, apellido: str, nota: int) -> dict:
    diccionario_Alumno = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "nota": nota
    }
    return diccionario_Alumno

def ingresar_alumno_lista(lista_alumno: list):
    dni = int(input("Ingrese el DNI: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    nota = int(input("Ingrese nota: "))
    
    diccionario_alumno = crear_alumno(dni, nombre, apellido, nota)
    
    lista_alumno.append(diccionario_alumno)

# R
def mostrar_un_alumno(un_alumno: dict):
    print(f"{un_alumno["dni"]:10}{un_alumno["apellido"]:12}{un_alumno["nombre"]:12}{un_alumno["nota"]:>4}")
    
def mostrar_todos_los_alumnos(lista_alumnos: list[dict]):
    for alumno in lista_alumnos:
        mostrar_un_alumno(alumno)

# U 
def modificar_alumnos(lista_alumno: list[dict], dni: int):
    for alumno in lista_alumno:
        if dni == alumno["dni"]:
            print("Alumno encontrado")
            nueva_nota = int(input("Ingrese la nueva nota: "))
            alumno["nota"] = nueva_nota
            break
# D

def eliminar_alumno(lista_alumno: list[dict], dni: int):
    eliminado = None
    for alumno in lista_alumno:
        if dni == alumno["dni"]:
            eliminado = alumno
            break
        
    if eliminado != None:
        lista_alumno.remove(eliminado) 
        
    return eliminado