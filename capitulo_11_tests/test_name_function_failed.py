import unittest
from name_function_failed import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Pruebas para name_function_failed.py"""

    def test_first_last_name(self):
        """¿Funcionarán nombres como linus torvalds?"""
        formatted_name = get_formatted_name('linus', 'torvalds')
        self.assertEqual(formatted_name, 'Linus Torvalds')

if __name__ == '__main__':
    unittest.main()