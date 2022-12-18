class User:
    """Clase que modela un usuario."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0
        self.phone_number = '111 222 333' # Valor por defecto
        self.email = ''

    def describe_user(self):
        "Imprime la información del usuario"
        print(f"El nombre y apellidos del usuario es {self.first_name} {self.last_name}")
        print(f"El usuario tiene {self.age} años.")
        print(f"Y sus datos de contacto son:")
        print(f"Teléfono: {self.phone_number} - Correo electrónico: {self.email}")

user1 = User('Manolo', 'López')
user1.age = 27
user1.email = 'manolo@usuario1.com'

user1.describe_user()