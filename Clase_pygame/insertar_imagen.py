import pygame  

pygame.init() # Inicializo pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)

ANCHO_VENATANA = 900
ALTO_VENTANA = 1500
TAMAÑO_VENTANA = (ALTO_VENTANA,ANCHO_VENATANA)

pygame.init()

ventana_ppal = pygame.display.set_mode(TAMAÑO_VENTANA)

pygame.display.set_caption("Prueba imagenes")

imagen = pygame.image.load("imgPygame.jpg")
otra_imagen = pygame.image.load("OIP.jpeg")
otra_imagen = pygame.transform.scale(otra_imagen, 200,200)#ANCHO= 200PX ALTO=200PX

flag_run = True
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
            
    ventana_ppal.blit(imagen,(0,0))
    ventana_ppal.blit(otra_imagen,(0,0))
    pygame.display.update()

pygame.quit()