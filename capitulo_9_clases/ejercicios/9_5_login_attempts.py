# Añade un atributo llamado login_attemps a tu clase User del ejercicio 9-3.
# Escribe un método llamado increment_login_attemps() que incremente el valor de login_attempts en 1.
# Escribe otro método llamado reset_login_attepmts() que resetée el valor de login_attempts a 0.
# Crea una instancia de la clase User y llama a increment_login_attempts() varias veces.
# Imprime el valor de login_attempts para asegurarte de que se incrementó adecuadamente,
# y luego llama a reset_login_attempts().
# Imprime login_attempts de nuevo para asegurarte de que se reseteó a 0.

class User:
    """Clase que modela el perfil de un usuario."""
    def __init__(self, first_name, last_name, age, address, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Imprime un resumen de la información del usuario."""
        print(f"- Nombre de usuario: {self.first_name}.")
        print(f"- Apellidos: {self.last_name}.")
        print(f"- Edad: {self.age}.")
        print(f"- Dirección: {self.address}.")
        print(f"- Número de teléfono: {self.phone_number}.")
        print(f"- Correo electrónico: {self.email}\n")

    def greet_user(self):
        print(f"\nHola {self.first_name}, se ha creado tu perfil de usuario.")
        print("ENHORABUENA!!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Guido', 'Van Rossum', 60, '25, La Runa st.', '111 222 333', 'guido@python.ned')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"El valor de login_attempts es: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"El valor actual de login attempts es: {user1.login_attempts}")