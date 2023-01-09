# Escribe una función que acepte dos parámetros: el nombre de una ciudad y el nombre de un país.
# La función debe devolver una cadena sencilla de la forma City, Country como Santiago, Chile.
# Almacena la función en un módulo llamado city_functions.py.
# Crea un fichero llamado test_cities.py que pruebe la función que acabas de escribir
# (recuerda que necesitas importar unittest y la función que quieras probar).
# Escribe un método llamado test_city_country() para verificar que el resultado de llamar a tu función
# con valores como ‘santiago’ y ‘chile’ devuelve la cadena correcta.
# Ejecuta test_cities.py y asegúrate de que test_city_country pase la prueba.

def get_formatted_city(city, country):
    """Devuelve una cadena con la ciudad y su país."""
    ciudad_pais = f"{city} {country}"
    return ciudad_pais.title()