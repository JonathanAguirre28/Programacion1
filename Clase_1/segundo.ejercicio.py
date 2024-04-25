###################FUNCIONES#####################
import random


def sumar_numeros_1():
    un_numero = input("Ingrese un numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese otro numero: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    print(f"La suma es: {suma}")
    
def sumar_numeros_2():
    un_numero = input("Ingrese un numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese otro numero: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    return suma

def sumar_numeros_3(un_numero, otro_numero):
    suma = un_numero + otro_numero
    
    print(f"La suma es: {suma}")
    
    
def sumar_numero_4(un_numero, otro_numero):
    suma = un_numero + otro_numero
    
    return suma
    
################MAIN#########################
#print("Bienvenidos a mi programa")
#sumar_numeros_1()
#print("Gracias por utilizar mi programa. Deje un cafecito")

#resultado = sumar_numeros_2()

#if resultado > 500:
#    print("Mayor")
#else:
#    print("Es menor")

#sumar_numeros_3(4, 9)

#un_numero = input("Ingrese un numero: ")

numero_1 = random.randint(1, 6)
numero_2 = random.randint(1, 6)

#sumar_numeros_3(numero_1, numero_2)

numero_1 = random.randint(1, 6)
numero_2 = random.randint(1, 6)
numero_3 = random.randint(1, 6)
numero_4 = random.randint(1, 6)

jugada_mati = sumar_numero_4(numero_1, numero_2)
jugada_ger = sumar_numero_4(numero_3, numero_4)

if jugada_ger > jugada_mati:
    print("Gano ger")
elif jugada_ger < jugada_mati:
    print("Gano mati")
else:
    print("Empataron")
    
    

    

    
    

