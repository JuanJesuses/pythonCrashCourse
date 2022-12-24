# Haz una clase Dice(dado) con un atributo llamado sides, que tenga un valor por defecto de 6.
# Escribe un método llamado roll_dice() que imprima un número aleatorio entre 1 y el número de caras que tiene el dado.
# Haz un dado de 6 caras y hazlo rodar 6 veces.
# Haz un dado de 10 caras y otro de 20 caras. Haz rodar cada uno 10 veces.

from random2 import randint

class Dice:
    """Clae que representa un dado."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(randint(1, self.sides))


dado = Dice()
dado10 = Dice(10)
dado20 = Dice(20)
"""
for i in range (6):
    dado.roll_dice()"""
"""
for i in range (10):
    dado10.roll_dice()"""

for i in range (10):
    dado20.roll_dice()