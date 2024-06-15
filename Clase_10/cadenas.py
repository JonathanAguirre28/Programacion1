cadena = "Hola a todos"

for i in range(5, len(cadena)):
    print(cadena[i], end = "")
    
print(type(cadena))
caracter = cadena[3]
print(caracter)

cadena = "L" + cadena[1:]


print(cadena)

print(cadena[3:]) #DESDE HASTA, EL DESDE HASTA, EL HASTA LO EXCLUYE
print(cadena[:8])

nombre = input("Ingrese su nombre: ")
while len(nombre) > 10:
    nombre = input("Reingrese su nombre: ")

cadena_1 = "Hola, "
cadena_2 = "Como estan?"
# cadena_3 = cadena_1 + " " + cadena_2
cadena_3 = f"{cadena_1} {cadena_2}"

for i in range(3):
    print(cadena_1)

print(cadena_1 * 3)

cadena = "hola"

print(cadena == "hola") # TRUE
print(cadena != "hola") # FALSE
print(cadena == "Hola") # FALSE

lista_nombres = ["Pepe", "Moni","ana","Coqui"]

for nombre in lista_nombres:
    print(nombre)

for i in range (0, len(nombres) - 1):
    for j in range(i + 1, len(nombres)):
        if nombres[i] < nombres[j]:
            auxiliar = nombres[i]
            nombres[i] = nombres[j]
            nombres[j] = auxiliar
print(nombres)
        

cadena = "Hola a todos"
contador_a = 0

for i in range(len(cadena)):
    if cadena[i] == "a":
        contador_a += 1

print(contador_a)    

def buscar_caracter(busqueda, cadena):
    encontro = False
    for i in range(len(cadena)):
        if cadena[i] == busqueda:
            encontro = True
            break
        
    return encontro


validos_validos = "ABCDEFGHIJKMNÑOPQRSTUVWXYZ"

cadena = "HoLa"
cadena_2 = ""
for i in range(len(cadena)):
    caracter = cadena[i]
    if buscar_caracter(caracter, validos_validos):
        caracter = chr(ord(caracter) + 32)
    cadena_2 += caracter

print(cadena_2)