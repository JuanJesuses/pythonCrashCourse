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

class ElectricCar(Car):
    """Reperesenta aspectos de un coche eléctrico."""

    def __init__(self, make, mdoel, year):
        """Inicializa los atributos de la clase padre."""
        super().__init__(make, mdoel, year)
        self.battery_size = 75

    def describe_battery(self):
        """Imprime una frase describiendo la batería."""
        print(f"Este coche tienen una batería de {self.battery_size} kWh.")

    def fill_gas_tank(self):
       """Sobreescribe el método del llenado de tanque en un coche no eléctrico."""
       print("los coches eléctricos no llevan depósito de conbustible, hijueputa.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_car = Car('Ford', 'Taurus', 1980)
my_car.fill_gas_tank(100)