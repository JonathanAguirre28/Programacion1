mi_lista= [False] * 5

bandera_seguir = True
while bandera_seguir:
    posicion = int(input("Ingrese la posicion: "))
    while posicion < 1 or posicion > len(mi_lista):
        posicion = int(input("Reingrese la posicion: "))
    numero = int(input("Ingrese un numero: "))
    
    mi_lista[posicion-1] = numero
    
    seguir = input("Desea ingresar otro (si/no)?: ")
    if seguir == "no":
        bandera_seguir = False
        
for i in range(len(mi_lista)):
    if mi_lista[i] != False:
        print(f"{i+1} -> {mi_lista[i]}")
