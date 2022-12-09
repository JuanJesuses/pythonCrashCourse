class Dog:
    """Un intento sencillo de modelar un perro."""
    def __init__(self, name, age):
        """Inicializa los atributos nombre y edad."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula a un perro sentándose respondiendo a un comando."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simula dar la vuelta respondiendo a un comando."""
        print(f"{self.name} rolled-over.")


my_dog = Dog('Nuble', 6)
your_dog = Dog('Willie', 7)

print(f"Mi perro se llama {my_dog.name}.")
print(f"Mi perro tiene {my_dog.age} años.")
my_dog.sit()

print(f"\nTu perro se llama {your_dog.name}.")
print(f"Tu perro tiene {your_dog.age} años.")
your_dog.sit()