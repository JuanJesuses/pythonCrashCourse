# Crea una clase llamada User. Crea dos atributos llamados first_name y last_name y a continuación,
# crea otros atributos que normalmente se almacenen en un perfil de usuario. Crea un método llamado describe_user()
# que imprima un resumen de la información del usuario.
# Crea otro método llamado greet_user() que imprima un saludo personalizado para el usuario.
# Crea varias instancias representando diferentes usuarios y llama a ambos métodos para cada usuario.

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


user1 = User('Guido', 'Van Rossum', 60, '25, La Runa st.', '111 222 333', 'guido@python.ned')
user2 = User('Linus', 'Torvalds', 56, '46, Aurora Boreal st.', '222 444 555', 'linus@linux.fi')
user3 = User('Richard', 'Stallman', 78, '115, La Milla rd.', '333 555 444', 'richard@stallman.com')
user4 = User('Alan', 'Turing', 92, '221B, Downing st.', '444 222 666', 'alan@turing.uk')
user5 = User('Ron', 'Von Neumann', 99, '36, Donnintong rd.', '555 666 777', 'ron@von.de')

user1.describe_user()
user2.describe_user()
user3.describe_user()
user4.describe_user()
user5.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()
user4.greet_user()
user5.greet_user()