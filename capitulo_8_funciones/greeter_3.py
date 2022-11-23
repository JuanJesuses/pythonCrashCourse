def get_formatted_name(first_name, last_name):
    """ Devuelve un nombre completo bien formateado. """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Esto es un bucle infinito!
while True:
    print("\nPor favor, introduce tu nombre: ")
    f_name = input('First name: ')
    l_name = input('Last name: ')

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHola, {formatted_name}!")