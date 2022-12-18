# Un puesto de helados es un tipo específico de restaurante. Escribe una clase llamada IceCreamStand que herede
# de la clase Restaurant que escribiste en el ejercicio 9-1 o en el 9-4. Cualquiera de las versiones de la clase
# funcionará, sólo elige la que más te guste. Añade un atributo llamado flavours que almacene una lista
# de sabores de helados. Escribe un método que muestre esos sabores.
# Crea una instancia de IceCreamStand y llama a este método.

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

class IceCreamStand(Restaurant):
    """Modela un tipo de restaurante dedicado a los helados."""
    def __init__(self, restaurant_name, cuisine_type): #, flavours
        """Representa aspectos de un tipo de restaurante dedicado a los helados."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def show_flavours(self):
        """Muestra una lista con los sabores de los helados."""
        num = 1
        for sabor in self.flavours:
            print(f"{num} - {sabor.title()}")
            num += 1


restaurante_postre = IceCreamStand('shanaya', 'árabe')
restaurante_postre.flavours = ['yogur', 'fresa', 'mango', 'stracciatela']
restaurante_postre.show_flavours()

