from user_9_12 import User
from privileges_9_12 import Privileges

class Admin(User):
    """Clase que modela el tipo de usuario administrador."""
    def __init__(self, first_name, last_name, age, address, phone_number, email):
        super().__init__(first_name, last_name, age, address, phone_number, email)
        self.privileges = Privileges()