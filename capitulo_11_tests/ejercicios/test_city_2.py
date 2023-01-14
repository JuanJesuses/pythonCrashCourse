import unittest
from population_11_2 import get_formatted_city

class CityTestCase(unittest.TestCase):
    """Pruebas para función ciudad, país, población"""

    def test_city_country_pop(self):
        formatted_name = get_formatted_city("almería,", "españa", "- population=5000000")
        self.assertEqual(formatted_name, "Almería, España - Population=5000000")