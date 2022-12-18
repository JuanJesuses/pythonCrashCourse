class Car:
    """un simple intento de representar un coche."""

    def __init__(self, make, model, year):
        """Inicializa los atributos para describir un coche."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devuelve un nombre descriptivo con formato ordenado."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Imprime una frase que muestra el kilometraje del coche."""
        print(f"Este coche tiene {self.odometer_reading} kilómetros.")

    def update_odometer(self, mileage):
        """Establece la lectura del cuentakilométros al valor dado.
           Rechaza el cambio si se intenta hacer retroceder el cuentakilómetros."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("no puedes retroceder el cuentakilómetros, hijueputa!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, amount):
        """Indica la cantida de combustible que tiene el coche"""
        self.amount = amount
        print(f"El coche tiene {self.amount} litros de gasolina.")

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

    def fill_gas_tank(self):
        """Los coches eléctricos no necesitan un tanque de gasolina."""
        print("Este coche no necesita un tanque de gasolina.")


#coche1 = Car('Ssang Yong', 'Rodius', 2015)
#coche1.fill_gas_tank(75)
#my_tesla.fill_gas_tank()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size = 100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()