"""Un conjunto de clases que puede ser usado para representar coches eléctricos."""
from car import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=100):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Imprime una frase acerca del alcance que proporciona esta batería."""
        if self.battery_size == 75:
            range = 418.43
        elif self.battery_size == 100:
            range = 506.94

        print(f"Este coche puede circular unos {range} kilómetros con una carga completa.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()