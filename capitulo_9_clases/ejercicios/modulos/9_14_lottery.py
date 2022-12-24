# Haz una lista o una tupla que contenga una serie de 10 números y cinco letras.
# Aleatoriamente, selecciona 4 números o letras de la lista e imprime un mensaje diciendo que cualquier boleto
# que coincida con esos cuatro números o letras ganará un premio.

import random2
from random2 import choice, randint
import string

lista_lottery = ['2', '18', '34', '1', '7', '45', '15', '3', '9', '20', 's', 'j', 't', 'f', 'h', 'a']
ticket_winner = []

for i in range (4):
    item_choice = choice(lista_lottery)
    ticket_winner.append(item_choice)

print(f"El boleto que coincida con los elementos: {ticket_winner}, será el ganador.")