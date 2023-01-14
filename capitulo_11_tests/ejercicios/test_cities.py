# Crea un fichero llamado test_cities.py que pruebe la función que acabas de escribir
# (recuerda que necesitas importar unittest y la función que quieras probar).
# Escribe un método llamado test_city_country() para verificar que el resultado de llamar a tu función
# con valores como ‘santiago’ y ‘chile’ devuelve la cadena correcta.
# Ejecuta test_cities.py y asegúrate de que test_city_country pase la prueba.

import unittest
from city_functions_11_1 import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """Pruebas para la función ciudad, país."""

    def test_city_country(self):
        """Prueba la función city_functions_11_1.py"""
        formatted_name = get_formatted_city('almería,', 'españa')
        self.assertEqual(formatted_name, 'Almería, España ')

    def test_city_country_population(self):
        """Prueba la función con la población"""
        formatted_name_pop = get_formatted_city('almería', 'españa', '- population=250000')
        self.assertEqual(formatted_name_pop, 'Almería, España - Population=250000')