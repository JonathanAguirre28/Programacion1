# numero = 10

# for i in range(numero, -1, -1):
#     print(i)

# numero = 10

# while numero != -1:
#     print(numero)
#     numero = numero -1

def mostrar_cuenta_regresiva(numero):
    if numero != -1: # si el numero no es menos -1, sigue.
        print(numero) #muestra el numero 
        mostrar_cuenta_regresiva(numero - 1) # llama el numero y le resta uno
        
mostrar_cuenta_regresiva(10)
        