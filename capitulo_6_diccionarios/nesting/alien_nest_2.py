# Creamos una lista vacía para almacenar los aliens.
aliens = []

# Generamos 30 aliens
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Mostramos los 5 primeros aliens
for alien in aliens[:5]:
    print(alien)

print("...")

# Mostramos cuántos aliens se han creado
print(f"Número total de aliens: {len(aliens)}")