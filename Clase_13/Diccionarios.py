diccionario = {
    "nombre" : "Juan",
    "edad" : 25,
    "cuidad" : "Bs As"
}

# print(diccionario["nombre"])
# print(diccionario["edad"])

diccionario["profesion"] = "Programador"

# valor = diccionario.pop("edad") #elimina le edad
# print(valor)
# print(diccionario)

# print(diccionario.keys()) # optengo solo las claves
# print(diccionario.values()) # optengo solo los valores
# print(diccionario.items()) # optengo clava, valor

# for clave in diccionario:
#     # print(clave) # me traigo las claves
#     print(diccionario[clave]) # me traigo las claves
#     # print(f"{clave}: {diccionario[clave]}") # me traigo las claves y el valor

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

