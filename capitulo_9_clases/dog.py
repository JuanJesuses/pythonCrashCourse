class Dog:
    """Un intento sencillo de modelar un perro."""

    def __int__(self, name, age):
        """Inicializa los atributos nombre y edad."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula a un perro sentándose respondiendo a un comando."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simula dar la vuelta respondiendo a un comando."""
        print(f"{self.name} rolled -over.")