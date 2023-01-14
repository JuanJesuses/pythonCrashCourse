# Escribe un caso de prueba para Employee.
# Escribe dos métodos de prueba, test_give_default_raise() y test_give_custom_raise().
# Usa el método setUp() para que no tengas que crear una instancia de nuevo empleado en cada método de prueba.
# Ejecuta tu caso de prueba y asegúrate de que los dos test pasan la prueba.

import unittest
from employee_11_3 import Employee

class TestNewEmployees(unittest.TestCase):
    """Pruebas para la clase Employee."""

    def setUp(self):
        """Crea empleados con nombre, apellidos y salario anual."""
        self.new_employee = Employee('Antonio', 'Banderas', 40000)

    def test_give_default_raise(self):
        """Comprueba si el salario por defecto es salario más 5000."""
        self.assertEqual(self.new_employee.give_raise(), 45000)

    def test_give_custom_raise(self):
        """Comprueba si se suma el salario más que el incremento por defecto."""
        self.assertEqual(self.new_employee.give_raise(16000), 56000)

if __name__ == '__main__':
    unittest.main()