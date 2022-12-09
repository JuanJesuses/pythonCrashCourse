# Crea una clase llamada Restaurant. El método __init__() para Restaurant debe almacenar dos atributos:
# restaurant_name y cuisine_type. Crea un método llamado describe_restaurant()
# que imprima esas dos partes de información y un método llamado open_restaurant() que imprima un mensaje
# indicando que el restaurante está abierto. Crea una instancia llamada restaurant de tu clase.
# Imprime los dos atributos individualmente y luego llama a ambos métodos.

class Restaurant:
    """Clase que modela un restaurante."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Imprime el nombre y el tipo de cocina del restaurante."""
        print(f"El restaurante se llama {self.restaurant_name}.")
        print(f"El tipo de cocina es {self.cuisine_type}. Muy rica.")

    def open_restaurant(self):
        """Imprime un mensaje diciendo que el restaurante está abierto."""
        print(f"El restaurante {self.restaurant_name} está abierto.")

# Creamos una instancia de la clase
restaurant = Restaurant("El Botillo", "Comida Nigeriana")
# Imprimimos los atributos de forma individual
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Llamamos a ambos métodos
restaurant.describe_restaurant()
restaurant.open_restaurant()