class Settings:
    """Una clase para guardar toda la configuración de Alien Invasion"""

    def __init__(self):
        """Inicializa la configuración del juego."""
        # Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuración de la nave
        self.ship_speed = 1.5

        # Configuración de las balas.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configuración del alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction de 1 representa derecha; -1 representa izquierda
        self.fleet_direction = 1
