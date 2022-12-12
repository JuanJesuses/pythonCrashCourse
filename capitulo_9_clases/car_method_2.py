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


