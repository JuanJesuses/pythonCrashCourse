# Escribe un bucle que pregunte a las personas por qué les gusta programar.
# Cada vez que alguien introduzca una razón, añade esa razón a un fichero que almacene todas las respuestas.

sigues = 's'

while sigues == 's':
    why = input('¿Por qué te gusta programar?: ')

    with open('prog_poll.txt', 'a') as file_object:
        file_object.write(f"{why}.\n")

    sigues = input('¿Preguntar a alguien más (s/n)?: ')