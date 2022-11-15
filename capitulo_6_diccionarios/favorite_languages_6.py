# Mostrar resultados sin repeticiones

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

print('Los siguientes lenguajes han sido mencionados: ')
for language in set(favorite_languages.values()):
    print(language.title())

languages = {'python', 'ruby', 'python', 'c'}
print(languages)