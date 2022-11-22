# Escribe una función llamada describe_city() que acepte el nombre de una ciudad y su país.
# La función debe imprimir una frase simple como Reykjavik está en Islandia. Da un valor por defecto al parámetro país.
# Llama a tu función con tres ciudades diferentes y al menos una de las cuales no esté en el país por defecto.

def describe_city(city, country='Finladia'):
    """ Imprime una frase indicando una ciudad y el país donde está. """
    print(f"\n{city.title()} está en {country.title()}.")

describe_city('Helsinki')
describe_city('Turku')
describe_city('Rovaniemi')
describe_city('Moscú', 'Rusia')