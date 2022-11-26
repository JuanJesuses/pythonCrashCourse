# Escribe una función llamada city_country() que tome el nombre de una ciudad y de su país.
# La función devolverá una cadena formateada como esta:
# “Santiago, Chile”
# Llama tu función con al menos tres pares ciudad-país, e imprime los valores devueltos.

def city_country(city, country):
    print(f'"{city.title()}, {country.title()}"')

city_country('paris', 'francia')
city_country('barcelona', 'españa')
city_country('helsinki', 'finlandia')