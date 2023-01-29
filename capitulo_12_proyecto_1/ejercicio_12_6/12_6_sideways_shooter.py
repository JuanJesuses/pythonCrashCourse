# Escribe un juego que coloque una nave en el lateral de la pantalla y permita al jugador moverla arriba y abajo.
# Haz que la nave dispare una bala y se mueva hacia la derecha por la pantalla cuando el jugador
# pulse la barra espaciadora. Asegúrate de que las balas se borran cuando desaparecen de la pantalla.

import sys
import pygame

from settings import Settings
from nave import Nave
from bullet import Bullet

class SidewayShooters:
    """Clase general para gestionar los recursos y el comportamiento del juego."""

    def __init__(self):
        """Inicializa el juego y crea recursos."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        """
        self.screen = pygame.display.set_mode((0,0),  pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height"""
        pygame.display.set_caption("SideWay ShooTers")

        self.nave = Nave(self) # El argumento self se refiere aquí a la instancia actual de SidewayShooters. Este es el
                               # parámetro que da a la nave acceso a los recursos del juego como por ejemplo, screen.
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Inicia el bucle principal del juego."""
        while True:
            self._check_events() # 1ª Permite comprobar si hay eventos de teclado
            self.nave.update() # 2º Actualiza la posición de la nave
            self._update_bullets()  # 3º Actualiza la posición de las balas
            self._update_screen() # 4º Se dibuja la nave en la pantalla

    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a las pulsaciones de teclas."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.nave.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.nave.moving_down = True
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
            elif event.key == pygame.K_q:
                sys.exit()

    def _check_keyup_events(self, event):
        """Responde a las liberaciones de teclas"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.nave.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.nave.moving_down = False

    def _fire_bullet(self):
        """Crea una bala y la añade al gurpo de balas."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Actualiza la posición de las balas y se deshace de las viejas."""
        # Actualiza la posición de las balas.
        self.bullets.update()

        # Se deshace de las balas que han desaparecido
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
            print(len(self.bullets))


    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        self.nave.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

if __name__ == '__main__':
    # Crea una instancia del juego y lo ejecuta.
    sidews = SidewayShooters()
    sidews.run_game()