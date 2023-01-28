# Haz un archivo Pygame que cree una pantalla vacía. En el bucle de eventos, imprime el atributo event.key
# siempre que se detecte un evento pygame.KEYDOWN.
# Ejecuta el programa y pulsa varias teclas para ver cómo responde Pygame.
import sys
import pygame

class key_events:
    """Clase que crea una pantalla vacía e imprime cosas."""

    def __init__(self):
        """Incializamos la pantalla."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Eventos")

        self.bg_color = (150, 140, 130)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def run_window(self):
        """Bucle para mostar la pantalla."""
        while True:
            self.screen.fill(self.bg_color)
            self._check_events()
            pygame.display.flip() # Hace visible la última pantalla dibujada


if __name__ == '__main__':
    ke = key_events()
    ke.run_window()