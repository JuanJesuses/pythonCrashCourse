# Comienza con tu programa del ejercicio 9-1. Añade un atributo llamado number_served con un valor predeterminado de 0.
# Crea una instancia de esta clase llamada restaurant.
# Imprime el número de clientes a los que ha servido el restaurante y luego cambia esta valor e imprímelo de nuevo.

# Añade un método llamado set_number_served() que te permita establecer el número de clientes que han sido servidos.
# Llama a este método con un nuevo número e imprime el valor otra vez.

# Añade un método llamado increment_number_served() que te permita incrementar el número de clientes
# que han sido atendidos. Llama a este método con el número que quieras que pueda representar cuántos clientes
# fueron atendidos en, digamos, un día de trabajo.

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

# Parte 1
restaurant = Restaurant('Casa Lola', 'Cocina gitana')
print(f"El restaurante ha atendido hoy a", restaurant.number_served, "clientes.")
restaurant.number_served = 12
print(f"El restaurante ha atendido hoy a", restaurant.number_served, "clientes.")

# Parte 2
restaurant.set_number_served(45)
print(f"El restaurante ha atendido hoy a", restaurant.number_served, "clientes.")

# Parte 3
restaurant.increment_number_served(15)
print(f"El restaurante ha atendido hoy a", restaurant.number_served, "clientes.")


