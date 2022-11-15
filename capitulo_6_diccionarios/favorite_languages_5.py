# Lista de todos los lenguajes de programación elegidos en nuestra encuesta de lenguajes de programación
# sin el nombre de las personas que han hecho cada elección.

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

print('Los siguientes lenguajes han sido mencionados: ')
for language in favorite_languages.values():
    print(language.title())