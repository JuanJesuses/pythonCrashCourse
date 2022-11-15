# Escoge un color para un alien como hiciste en el ejercicio 5-3 y escribe una cadena if-else.

alien_color = 'red'

# 1. Si el color del alien es verde, imprime una frase que indique que el jugador acaba de ganar 5 puntos
# por disparar al alien.
if alien_color == 'green':
    print('¡¡¡Enhorabuena, has ganado 5 puntos!!!')
# 2. Si el color del alien no es verde, imprime una frase que indique que el jugador acaba de ganar 10 puntos.
else:
    print('¡¡¡Enhorabuena, has ganado 10 puntos!!!')

# 3. Escribe una versión de este programa que ejecute un bloque if y otra que ejecute un bloque else.
if alien_color == 'red':
    print('Vamos a ejecutar el bloque if.')
else:
    print('No vamos a ejecutar el bloque else.')

if alien_color != 'red':
    print('No vamos a ejecutar el bloque if')
else:
    print('Vamos a ejecutar el bloque else.')