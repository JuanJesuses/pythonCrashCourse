import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Una clase para disparar las balas desde la nave."""

    def __init__(self, sidews_game):
        """Crea un objeto para la bala en la posición actual de la nave."""
        super().__init__()
        self.screen = sidews_game.screen
        self.settings = sidews_game.settings
        self.color = self.settings.bullet_color

        # Crea un rectángulo para la bala en (0,0) y luego establece la posición correcta.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height) # Como las balas no son imágenes creamos un rectángulo
                                                             # cero con la clase pygame.Rect()
        self.rect.midright = sidews_game.nave.rect.midright

        # Guarda la posición de la bala con el valor decimal.
        self.x = float(self.rect.x)

    def update(self):
        """Mueve la bala hacia arriba por la pantalla."""
        # Actualiza la posición decimal de la bala
        self.x += self.settings.bullet_speed
        # Actualiza la posición del rectángulo
        self.rect.x = self.x

    def draw_bullet(self):
        """Dibuja la bala en la pantalla."""
        pygame.draw.rect(self.screen, self.color, self.rect)