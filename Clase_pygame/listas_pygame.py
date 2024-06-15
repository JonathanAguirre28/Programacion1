import pygame  

lista_nombres = ["Jonathan", "Adrian", "Aguirre", "Simon"]

pygame.init() # Inicializo pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)

ventana = pygame.display.set_mode((1500, 900)) # Alto y ancho de la ventana (píxeles)
pygame.display.set_caption("Mi primer ventana") # Título de la ventana

# Cargo una imagen para el icono y para el fondo
icono = pygame.image.load("imgPygame.jpg")
pygame.display.set_icon(icono)

# Cargo la imagen de fondo
fondo = pygame.transform.scale(icono, (1500, 900))

fuente = pygame.font.SysFont("consolas",50) #Definir la configuracion de la fuente
texto = fuente.render("Bienvenidos a Joni bross", False, BLANCO, AZUL_CLARO)
# subtexto = fuente.render("PLAY",False,BLANCO, AZUL_CLARO)

flag = True
while flag: # Bucle infinito
    y = 50
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: # Pregunto si presionó la 'x' de la ventana
            flag = False

    for nombre in lista_nombres:
        texto = fuente.render(nombre, False, BLANCO, AZUL_CLARO)
    # Dibujo la imagen de fondo
        # ventana.blit(fondo, (0, 0))
        ventana.blit(texto,(50,y))
        y += 60

    pygame.display.update() # Actualizo la pantalla

pygame.quit() # Finaliza pygame
