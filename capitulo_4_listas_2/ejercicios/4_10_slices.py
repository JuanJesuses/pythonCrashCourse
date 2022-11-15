# Utilizando uno de los programas escritos en este capítulo, añade más líneas al final del programa
# que hagan lo siguiente:

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# 1. Imprime el mensaje ‘Los primeros tres elementos de la lista son: ’.
# Luego utiliza un slice para imprimir los tres primeros elementos de la lista de ese programa.
print('Los tres primeros jugadores de la lista son: ')
print(players[:3])

# 2. Imprime el mensaje ‘Los elementos que se encuentran en medio de la lista son: ’.
# Luego utiliza un slice para imprimir los elementos que se encuentran en medio de la lista de ese programa.
print('\nLos tres jugadores que se encuentran en medio de la lista son: ')
print(players[1:4])

# 3. Imprime el mensaje ‘Los últimos tres elementos de la lista son: ’.
# Luego utiliza un slice para imprimir los tres últimos elementos de la lista de ese programa.
print('\nLos tres últimos jugadores de la lista son: ')
print(players[-3:])