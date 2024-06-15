import pygame

#colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)


ANCHO_VENTANA = 800
ALTO_VENTANA = 800

DIMENSION_VENTANA = (ANCHO_VENTANA, ANCHO_VENTANA)

pygame.init()

ventana = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Comision 311")
icono = pygame.image.load("Imagenes\\utn_icono.jpg")
pygame.display.set_icon(icono)

#GATITO
gatito = pygame.image.load("Imagenes\\gatito.jpeg")
# gatito = pygame.transform.scale(gatito, DIMENSION_VENTANA)#Cubre toda la pantalla
gatito = pygame.transform.scale(gatito, (100,100))
gatito_rectangulo = gatito.get_rect()
gatito_rectangulo.topleft = (50,650)

#TEXTO
fuente = pygame.font.SysFont("consolas", 20)
texto = fuente.render("Miau, Miau", True, AZUL, VERDE)

ventana.fill(BLANCO)

bandera_texto = False
bandera = True
while bandera:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: # esto es un evento
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if gatito_rectangulo.collidepoint(evento.pos):
                bandera_texto = True
            
    ventana.blit(gatito, gatito_rectangulo)
    if bandera_texto:
        ventana.blit(texto, (300,100))
        
        
    pygame.display.update()



pygame.quit() #metodo que finaliza pygame