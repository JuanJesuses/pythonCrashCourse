# Vamos a rastrear la posición de un alien que puede moverse a diferentes velocidades.

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Posición original: {alien_0['x_position']}")

# Mueve el alien a la derecha.
# Determinar los lejos que se ha movido el alien en base a su velocidad actual.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Esto debe ser un alien rápido
    x_increment = 3

# La nueva posición es la nueva posición más el incremento.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"Nueva posición: {alien_0['x_position']}")

alien_0['speed'] = 'fast'