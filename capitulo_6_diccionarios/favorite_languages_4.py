# Ordenar las claves a medida que van siendo devueltas en el bucle.
# Puedes utilizar la función sorted() para obtener una copia de las claves en orden.

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, gracias por hacer la encuesta.")