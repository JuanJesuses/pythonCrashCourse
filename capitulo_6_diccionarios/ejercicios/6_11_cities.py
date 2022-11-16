# Haz un diccionario llamado cities. Usa el nombre de tres ciudades como claves de tu diccionario.
# Crea un diccionario de información de cada ciudad e incluye el país donde está esa ciudad, su población aproximada
# y un dato de la ciudad.
# Las claves para cada diccionario de ciudades podría ser algo como country, population and fact.
# Imprime el nombre de cada ciudad y toda la información que hayas almacenado sobre ella.

cities = {
    'toronto' : {
        'país' : 'canadá',
        'población' : 5113149,
        'hechos' : 'Tiene la vecindad más insólita llamada Distillery District'
    },
    'helsinki' : {
        'país' : 'finlandia',
        'población' : 1402394,
        'hechos' : 'Los días duran menos de seis horas durante el solsticio de invierno'
    },
    'chicago' : {
        'país' : 'eeuu',
        'población' : 9500000,
        'hechos' : 'La torre Willis salió en la película Poltergeist 3'
    }
}

for city, info in cities.items():
    print(f"\nEsta es la ciudad de {city.title()}:")
    for dato, respuesta in info.items():
        print(f"\t{dato.title()} : {respuesta}." )