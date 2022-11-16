# Haz un diccionario llamado favorite_places. Piensa tres nombres para usar como claves en el diccionario
# y almacena de uno a tres lugares favoritos para cada persona. Para hacer este ejercicio un poco más interesante,
# pregunta a algunos amigos el nombre de unos cuantos de sus lugares favoritos.
# Recorre el diccionario e imprime el nombre de cada persona y sus lugares favoritos.

favorite_places = {
    'juan' : ['sillicon valley', 'comic con', 'finlandia'],
    'raquel' : ['santorini', 'brujas'],
    'álvaro' : ['londres', 'el puche', 'galicia'],
    'alex' : ['barcelona', 'manchester'],
}

for nombre, lugares in favorite_places.items():
    print(f"\nLos lugares favoritos de {nombre.title()} son:")
    for lugar in lugares:
        print(f"\t{lugar.title()}")