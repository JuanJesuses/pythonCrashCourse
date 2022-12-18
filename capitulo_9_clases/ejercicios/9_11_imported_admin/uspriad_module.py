class User:
    """Clase que modela el perfil de un usuario."""
    def __init__(self, first_name, last_name, age, address, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def describe_user(self):
        """Imprime un resumen de la información del usuario."""
        print(f"\n- Nombre de usuario: {self.first_name}.")
        print(f"- Apellidos: {self.last_name}.")
        print(f"- Edad: {self.age}.")
        print(f"- Dirección: {self.address}.")
        print(f"- Número de teléfono: {self.phone_number}.")
        print(f"- Correo electrónico: {self.email}\n")

    def greet_user(self):
        print(f"Hola {self.first_name}, se ha creado tu perfil de usuario.")
        print("ENHORABUENA!!")

class Privileges:
    """Describe los privilegios de los usuarios."""
    def __init__(self):
        self.privileges = ["Puede añadir un post", "Puede eliminar un post", "Puede añadir un usuario", "Puede eliminar un usario"]

    def show_privileges(self):
        """Muestra los privilegios del usuario admin."""
        num = 1
        for privilege in self.privileges:
            print(f"{num} - {privilege}.")
            num += 1

class Admin(User):
    """Clase que modela el tipo de usuario administrador."""
    def __init__(self, first_name, last_name, age, address, phone_number, email):
        super().__init__(first_name, last_name, age, address, phone_number, email)
        self.privileges = Privileges()