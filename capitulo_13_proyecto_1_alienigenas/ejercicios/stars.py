import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Una clase que representa una estrella en el firmamento."""

    def __init__(self, ai_game):
        """Inicializa las estrellas y configura su posición inicial."""
        super().__init__()
        self.screen = ai_game.screen

        #Carga la imagen de la estrella y configura su rectángulo
        self.image = pygame.image.load('../alien_invasion/images/strato.png')
        self.rect = self.image.get_rect()

        # Comienza cada estrella en parte central de la pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacena la estrella en la posición (ya veremos) exacta.
        self.x = float(self.rect.x)

