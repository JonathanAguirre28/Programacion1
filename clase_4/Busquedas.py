lista = [7,-9,7,-6,-1,7,-2,1]

bandera = False
for i in range(len(lista)):
    if lista[i] < 0:
        bandera = True
        break
    
if bandera == True:
    print("Por lo menos hay un negativo")
else:
    print("No hay negativos")