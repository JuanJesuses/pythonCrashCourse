# magina un alien que acaba de ser eliminado en un juego. Crea una variable llamada alien_color
# y asígnale un valor de ‘green’, ‘yellow’ o ‘red’.

alien_color = 'red'

# 1. Escribe una sentencia if para comprobar si el color del alien es verde.
# Si lo es, imprime un mensaje que indique que el jugador acaba de ganar 5 puntos.

if alien_color == 'green':
    print('¡¡¡Enhorabuena, has ganado 5 puntos!!!')

# 2. Escribe una versión de este programa que pase una prueba if y otra que no lo haga
# (la versión que falle no tendrá salida).

if alien_color == 'red':
    print('¡¡¡Enhorabuena, has ganado 5 puntos!!!')

if alien_color != 'red':
    alien_color = 'red'