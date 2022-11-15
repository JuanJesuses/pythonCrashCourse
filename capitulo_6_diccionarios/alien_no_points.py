# Veamos qué ocurre cuando buscamos la puntuación de un alien que no tienen configurada dicha puntuación.
# print(alien_0['points'])

alien_0 = {'color' : 'green', 'speed' : 'slow'}

point_value = alien_0.get('points', 'No hay puntuación asignada.')
print(point_value)

