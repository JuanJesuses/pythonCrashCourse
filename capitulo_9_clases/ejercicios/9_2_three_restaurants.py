# Comienza tu clase desde el ejercicio 9-1. Crea tres instancias diferentes de la clase
# y llama a describe_restaurant() para cada instancia.

class Restaurant:
    """Clase que modela un restaurante."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Imprime el nombre y el tipo de cocina del restaurante."""
        print(f"\nEl restaurante se llama {self.restaurant_name}.")
        print(f"El tipo de cocina es {self.cuisine_type}. Muy rica.")

    def open_restaurant(self):
        """Imprime un mensaje diciendo que el restaurante está abierto."""
        print(f"El restaurante {self.restaurant_name} está abierto.")

# Creamos la instancia uno
restaurant = Restaurant('El Botillo', 'Cocina Nigeriana')

# Creamos la instancia dos
restaurant2 = Restaurant('Senza Pomodoro', 'Cocina Italiana')

# Creamos la instancia tres
restaurant3 = Restaurant('La Paca', 'Cocina Española')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()