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