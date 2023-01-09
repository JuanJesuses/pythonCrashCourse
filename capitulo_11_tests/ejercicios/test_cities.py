# Crea un fichero llamado test_cities.py que pruebe la función que acabas de escribir
# (recuerda que necesitas importar unittest y la función que quieras probar).
# Escribe un método llamado test_city_country() para verificar que el resultado de llamar a tu función
# con valores como ‘santiago’ y ‘chile’ devuelve la cadena correcta.
# Ejecuta test_cities.py y asegúrate de que test_city_country pase la prueba.

import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """Pruebas para la función ciudad, país."""

    def test_city_country(self):
        """Prueba la función city_functions.py"""
        formatted_name = get_formatted_city('almería,', 'españa')
        self.assertEqual(formatted_name, 'Almería, España')