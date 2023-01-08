import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Pruebas para name_function.py"""

    def test_first_last_name(self):
        """¿Funcionan nombres como Linus Torvalds?"""
        formatted_name = get_formatted_name('linus', 'torvalds')
        self.assertEqual(formatted_name, 'Linus Torvalds')

if __name__ == '__main__':
    unittest.main()