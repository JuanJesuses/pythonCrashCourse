import pygame

class Cobete:
    """Clase que modela el cobete."""

    def __init__(self, rc_cobete):
        """Inicializa la nave y configura su posición inicial."""
        self.screen = rc_cobete.screen
        self.settings = rc_cobete.setting
        self.screen_rect = rc_cobete.screen.get_rect()

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Colocamos la nave en el centro de la pantalla.
        self.rect.center = self.screen_rect.center

        # Guarda un valor decimal para la posición horizontal y vertical de la nave
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Bandera de movimiento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Actualiza la posición de la nave en función de la bandera de movimiento."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Actualiza el objeto rect de self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # Dibuja la nave en su posición actual.
        self.screen.blit(self.image, self.rect)