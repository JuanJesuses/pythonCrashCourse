import pygame
import sys

pygame.init()

imagen = pygame.image.load('alien_invasion/images/star.bmp')

pantalla = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Prueba estrellas')
rect_pantalla = pantalla.get_rect()
rect_imagen = imagen.get_rect()

x = rect_pantalla.x
y = rect_pantalla.y + 100

# ubicacion = (x, y)

bg_color = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pantalla.fill(bg_color)
    for i in range (5):
        if rect_imagen.x < 1200:
            ubicacion = (x, y*i)
            pantalla.blit(imagen, ubicacion)
    pygame.display.update()