# Puedes usar un bucle para comprobar lo difícil que puede ser ganar el tipo de lotería que acabas de modelar.
# Haz una lista o una tupla llamada my_ticket. Escribe un bucle que siga tirando números hasta que gane tu boleto.
# Imprime un mensaje que informe cuantas veces ha tenido que ejecutarse el bucle para darte un boleto ganador.


from random2 import choice

lista_lottery = ['2', '18', '34', '1', '7', '45', '15', '3', '9', '20', 's', 'j', 't', 'f', 'h', 'a']
ticket_winner = []

my_ticket = ['a', '18', '45', 'j']
contador = 0

while my_ticket != ticket_winner:
    # Generamos el boleto aleatoriamente
    for i in range(4):
        item_choice = choice(lista_lottery)
        ticket_winner.append(item_choice)
    # Si el boleto no coincide con el nuestro, incrementamos el contador y reincializamos el boleto.
    if ticket_winner != my_ticket:
        contador += 1
        ticket_winner = []

print(f"\nEl boleto ganador es {ticket_winner}.")
print(f"Sólo has necesitado {contador} intentos para ganar la lotería.")