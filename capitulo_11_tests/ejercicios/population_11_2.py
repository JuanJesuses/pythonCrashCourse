# Modifica tu función para que requiera un tercer parámetro, población.
# Ahora tiene que devolver una sencilla cadena de la forma
# City, Country – population xxx, como Santiago, Chile – population 5000000. Ejecuta test_cities.py de nuevo.
# Asegúrate de que test_city_country() falla esta vez.
# Modifica la función para que el parámetro population sea opcional.
# Ejecuta test_cities.py otra vez y asegúrate de que test_city_country() pasa de nuevo.
# Escribe un segundo test llamado test_city_country_population() que verifique que puedes llamar a tu función
# con los valores ‘santiago’, ‘chile’ y ‘population=5000000’.
# Ejecuta test_cities.py de nuevo y asegúrate de que el nuevo test pase.

def get_formatted_city(city, country, population):
    """Devuelve una cadena con la ciudad y su país."""
    ciudad_pais = f"{city} {country} {population}"
    return ciudad_pais.title()


resultado = get_formatted_city('almería,', 'españa', ' - population=5000000')

print(resultado)