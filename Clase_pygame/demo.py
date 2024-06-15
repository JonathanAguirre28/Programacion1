import sys
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

ventana_ppal.fill(BLANCO)

# pygame.draw.line(ventana_ppal, ROJO, (100,100), (350,100), (5))
# pygame.draw.line(ventana_ppal, AZUL, (100,100), (350,250), (5))
# pygame.draw.line(ventana_ppal, VERDE, (100,400), (350,300), (5))

# pygame.draw.line(ventana_ppal, NEGRO, (100,200), (100,300),5)

# pygame.draw.rect(ventana_ppal, VERDE,(50,50,100,100),5) #Cuadrado sin relleno
# #Los dos primeros valores son donde esta posicionado el cuadrado, los dos segundos valores son el ancho y alto
# pygame.draw.rect(ventana_ppal, VERDE,(150,150,100,300),5)

# pygame.draw.circle(ventana_ppal, ROJO, (60,60), 50,2) #Circulo

# pygame.draw.ellipse(ventana_ppal, AZUL, (50,50,200,100),2) #ECLIPSE
# pygame.draw.ellipse(ventana_ppal, AZUL, (250,100,200,300)) #ECLIPSE

# punto = [(100,300) (100,100), (150,120)]

# pygame.draw.polygon(ventana_ppal, AZUL, punto, 2)




flag_run = True
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()

pygame.quit()