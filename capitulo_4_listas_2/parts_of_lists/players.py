# Como con la función range(), Python se detiene un elemento antes del segundo índice que especifiquemos, es decir,
# si introducimos el rango lista[1:4], podremos trabajar con los elementos que se encuentren
# en las posiciones 1,2 y 3. Veamos el siguiente ejemplo.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

# Si no se indica el primer índice, Python empezará a trabajar desde el principio de la lista
print(players[:3])

# Lo mismo ocurre si queremos llegar al final de la lista desde un índice en concreto. Basta on indicar
# el primer índice en el devanado y dejar el segundo índice en blanco
print(players[2:])

print(players[-3:])

print('\nAquí están los tres primeros jugadores de mi equipo: \n')
for player in players[:3]:
    print(player.title())