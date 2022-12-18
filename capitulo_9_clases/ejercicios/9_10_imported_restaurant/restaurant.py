class Restaurant:
    """Clase que modela un restaurante."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Imprime el nombre y el tipo de cocina del restaurante."""
        print(f"El restaurante se llama {self.restaurant_name}.")
        print(f"El tipo de cocina es {self.cuisine_type}. Muy rica.")
        print(f"El restaurante ha atendido a {self.number_served} clientes hoy.")

    def open_restaurant(self):
        """Imprime un mensaje diciendo que el restaurante está abierto."""
        print(f"El restaurante {self.restaurant_name} está abierto.")

    def set_number_served(self, number_served):
        """Establece el número de clientes que han sido servidos."""
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment