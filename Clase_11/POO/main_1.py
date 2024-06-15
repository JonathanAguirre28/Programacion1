from class__personajes import *

def mostrar_lista_heroes(lista):
    for heroe in lista_heroes:
        if isinstance(heroe, Personaje):
            print(heroe.presentarse())
    
    

personaje_1 = Personaje(5, "Iroman", True, True, "Disparo ultrasonico", 1000)
personaje_2 = Personaje(1, "BlackWidow", False, False, "Ataque cuerpo a cuerpo", 900)
personaje_3 = Personaje(3, "Hulk", False, False, "Aplasta", 1500)
personaje_4 = Personaje(8, "Cap. America", False, False, "Fuerza extrema papota", 2000)


lista_heroes = []


lista_heroes.append(personaje_1)
lista_heroes.append(personaje_2)
lista_heroes.append(personaje_3)

mostrar_lista_heroes(lista_heroes)

lista_heroes.insert(2,personaje_4)

mostrar_lista_heroes(lista_heroes)

print(len(lista_heroes))

indice = 1

removido:Personaje = lista_heroes.pop(indice)

print(f"Quedo fuera de los avengers: {removido.nombre}")

mostrar_lista_heroes(lista_heroes)



# for i in range(len(lista_heroes)):
#     print(lista_heroes[i].presentarse())







# print(personaje_1.presentarse())

# personaje_1.Volar(1500, 100)

# personaje_1.poder_pelea -= 200

# print(personaje_2.presentarse())

# personaje_2.Volar(100, 80)

# print("\n")

# personaje_2.atacar(personaje_1)

# print(personaje_1.poder_pelea)
# print(personaje_2.poder_pelea)