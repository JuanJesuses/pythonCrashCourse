import pygame

class Nave():
    """Clase para gestionar la nave."""

    def __init__(self, sidews_game):
        """Inicializa la nave y configura su posición inicial."""
        self.screen = sidews_game.screen
        self.screen_rect = sidews_game.screen.get_rect()
        self.settings = sidews_game.settings

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load("images/nave.bmp")
        self.rect = self.image.get_rect()

        # Coloca la nave inicialmente en el centro de la parte lateral izquierda de la pantalla
        self.rect.midleft = self.screen_rect.midleft

        # Guarda un valor decimal para la posición vertical de la nave.
        self.y = float(self.rect.y)

        # Bandera de movimiento
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Actualiza la posición de la nave en función de la bandera de movimiento."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.velocidad_nave
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: # Si usasemos elif, la tecla flecha arriba siempre tendría prioridad
            self.y += self.settings.velocidad_nave

        # Actualiza el objeto rect de self.y
        self.rect.y = self.y

    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)