# Ahora estamos trabajando con ejemplos lo suficientemente complejos como para que se puedan ampliar de muchas maneras.
# Utiliza un programa de ejemplo de este capítulo y amplíalo añadiendo nuevas claves y valores,
# cambiando el contexto del programa y mejorando el formato de salida.
# Escojo el alien_no_points

alien_0 = {'color' : 'green', 'speed' : 'slow', 'points' : 5, 'mode' : 'easy'}
alien_1 = {'color' : 'yellow', 'speed' : 'medium', 'points' : 10, 'mode' : 'medium'}
alien_2 = {'color' : 'red', 'speed' : 'fast', 'points' : 15, 'mode' : 'hard'}
alien_3 = {'color' : 'purple', 'speed' : 'hiperloop', 'points' : 20, 'mode' : 'very hard'}

intruders = {
    'level 1' : alien_0,
    'level 2' : alien_1,
    'level 3' : alien_2,
    'level 4' : alien_3,
}

for nivel, tipos in intruders.items():
    print(f"\nSi estás en el {nivel}, la dificultad es {tipos.get('mode').title()}\ny estas son las características:")
    for tipo, valores in tipos.items():
        print(f"{tipo} : {valores}")