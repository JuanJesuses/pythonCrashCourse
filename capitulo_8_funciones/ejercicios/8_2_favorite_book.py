# Escribe una función llamada favortie_book() que acepte un parámetro, title.
# La función podría imprimir un mensaje como ‘Uno de mis libros favoritos es Alicia en el país de las maravillas’.
# Llama a la función y asegúrate de incluir el título del libro como argumento en la llamada a la función.

def favorite_book(title):
    """Muestra por pantalla el título del libro pasado por parámetro."""
    print(f"Uno de mis libros favoritos es {title.title()}")

favorite_book('Lord of the rings')