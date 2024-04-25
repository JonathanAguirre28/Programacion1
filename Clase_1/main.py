#from funciones import sumar_dos_numeros #Para importar solo la funcion
#import funciones #Para importar todo el modulo
#import package_aritmeticas.funciones as F #trae todo las vareables funciones (ALIAS SE LLAMA)


#un_numero = F.sumar_dos_numeros()
#print(un_numero)

import pygame

pygame.display.set_mode([500,500])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.display.update()    

import random 

print(random.randint(1,10))

lista = ["Cola-cola", "Fanta", "Fernet"]

opcion = random.choice(lista)

print(opcion)