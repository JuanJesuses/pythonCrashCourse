# Escribe una clase llamada Employee. El método __init_() debe tomar un primer nombre, un apellido, un salario anual
# y almacenar cada uno de esos atributos.
# Escribe un método llamado give_raise() que añada 5,000 € al salario anual por defecto,
# pero que también acepte un aumento de una cantidad diferente.
# Escribe un caso de prueba para Employee.
# Escribe dos métodos de prueba, test_give_default_raise() y test_give_custom_raise().
# Usa el método setUp() para que no tengas que crear una instancia de nuevo empleado en cada método de prueba.
# Ejecuta tu caso de prueba y asegúrate de que los dos test pasan la prueba.

class Employee():
    """Clase que modela un empledo."""

    def __init__(self, first, last, salary):
        """Almacena nombre, apellido y salario anual del empleado."""
        self.first_name = first
        self.last_name = last
        self.annual_salary = salary

    def give_raise(self, increment=5000):
        """Añade 5,000 € al salario anual por defecto."""
        salario = self.annual_salary + increment
        return salario

    def mostar_datos(self):
        print(f"Nombre: {self.first_name}")
        print(f"Apellidos: {self.last_name}")
        print(f"Salario = {self.annual_salary}")


