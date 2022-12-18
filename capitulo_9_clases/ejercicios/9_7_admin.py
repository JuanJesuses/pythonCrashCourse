# Un administrador es un tipo especial de usuario.
# Escribe una clase llamada Admin que herede de la clase User que escribiste en el ejercicio 9-3 o 9-5.
# Añade un atributo, privileges, que almacene una lista de cadenas como “puede añadir un post”,
# “puede eliminar un post”, “puede banear a un usuario”, etc.
# Escribe un método llamado show_privileges() que liste el conjunto de privilegios del administrador.
# Crea una instancia de Admin y llama a tu método.

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
        print(f"- Nombre de usuario: {self.first_name}.")
        print(f"- Apellidos: {self.last_name}.")
        print(f"- Edad: {self.age}.")
        print(f"- Dirección: {self.address}.")
        print(f"- Número de teléfono: {self.phone_number}.")
        print(f"- Correo electrónico: {self.email}\n")

    def greet_user(self):
        print(f"\nHola {self.first_name}, se ha creado tu perfil de usuario.")
        print("ENHORABUENA!!")

class Admin(User):
    """Clase que modela el tipo de usuario administrador."""
    def __init__(self, first_name, last_name, age, address, phone_number, email):
        super().__init__(first_name, last_name, age, address, phone_number, email)
        self.privileges = ["Puede añadir un post", "Puede eliminar un post", "Puede añadir un usuario", "Puede eliminar un usario"]

    def show_privileges(self):
        """Muestra los privilegios del usuario admin."""
        num = 1
        for privilege in self.privileges:
            print(f"{num} - {privilege}.")
            num += 1

user_admin2 = Admin('Linus', 'Torvalds', 56, '46, Aurora Boreal st.', '222 444 555', 'linus@linux.fi')
user_admin2.show_privileges()

user_admin2.greet_user()
user_admin2.describe_user()