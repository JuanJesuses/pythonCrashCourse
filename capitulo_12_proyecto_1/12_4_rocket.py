# Haz un juego que empiece con un cohete en el centro de la pantalla.
# Permita al jugador moverlo hacia arriba, hacia abajo, hacia la derecha y hacia la izquierda
# usando las cuatro teclas de dirección.
# Asegúrate de que el cohete nunca sobrepasa los bordes de la pantalla.
import sys
import pygame

from settings import Settings
from cobete import Cobete

class Rocket:
    """Clase que modela un cohete."""

    def __init__(self):
        """Inicializa los recursos del jusego."""
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("El Cobete")

        self.cobete = Cobete(self)

    def run_game(self):
        while True:
            self._check_events()
            self.cobete.update()
            self._update_screen()

    def _check_events(self):
        """Método para controlar los eventos de teclado y ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_events_keyup(event)


    def _check_events_keydown(self, event):
        """Método para gestionar eventos de keydown."""
        if event.key == pygame.K_RIGHT:
            self.cobete.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.cobete.moving_left = True
        elif event.key == pygame.K_UP:
            self.cobete.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.cobete.moving_down = True


    def _check_events_keyup(self, event):
        """Método para gestionar eventos KEYUP."""
        if event.key == pygame.K_RIGHT:
            self.cobete.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.cobete.moving_left = False
        elif event.key == pygame.K_UP:
            self.cobete.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.cobete.moving_down = False

    def _update_screen(self):
        """Método para actualziar la pantalla."""
        self.screen.fill(self.setting.bg_color)
        self.cobete.blitme() # Dibuja la imagen en la pantalla en la posición especificada por self.rect

        pygame.display.flip() # Hace visible la última pantalla dibujada

if __name__ == '__main__':
    rc = Rocket()
    rc.run_game()