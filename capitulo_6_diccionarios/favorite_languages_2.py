favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

# Estos dos bucle se comportan exactamente igual
for name in favorite_languages:
    print(name.title())

for name in favorite_languages.keys():
    print(name.title())

# este bucle recorre todos los items del diccionario y los muestra.
for name, language in favorite_languages.items():
    print(f"El lenguaje favortio de {name.title()} es {language.title()}.")