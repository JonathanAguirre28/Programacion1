import pygame  

pygame.init() # Inicializo pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)

ANCHO_VENATANA = 1500
ALTO_VENTANA = 900
TAMAÑO_VENTANA = (ANCHO_VENATANA,ALTO_VENTANA)

pygame.init()

ventana_ppal = pygame.display.set_mode(TAMAÑO_VENTANA)

pygame.display.set_caption("Prueba imagenes")

imagen = pygame.image.load("deadpool.jpg")

imagen = pygame.transform.scale(imagen,(300,300))

x = 0
flag_run = True
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False 
    ventana_ppal.blit(imagen,(x,50))
    x += 300
    if x >= ANCHO_VENATANA: #Controlando los valores de x y vamos a poder controlar los personajes que no desborden la pantalla
        x = 0 
    pygame.display.update()

pygame.quit()