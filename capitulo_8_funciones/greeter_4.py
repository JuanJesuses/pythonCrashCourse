def get_formatted_name(first_name, last_name):
    """ Devuelve un nombre completo bien formateado. """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Esto es un bucle infinito!
while True:
    print("\nPor favor, introduce tu nombre: ")
    print('(Introduce "q" para salir)')

    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHola, {formatted_name}!")