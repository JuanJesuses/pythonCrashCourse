import pygame

class Settings:
    """ Clase para guardar la configuración de los elementos del juego """

    def __init__(self):
        # Inicializa la configuración del juego
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (240, 230, 220)

        # Configuración de la nave
        self.velocidad_nave = 1.5

        # Configuración de las balas
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3