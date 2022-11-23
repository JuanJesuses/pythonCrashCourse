def get_formatted_name(first_name, last_name, middel_name=''):
    """ Devuelve un nombre completo con un formato ordenado. """
    if middel_name:
        full_name = f"{first_name} {middel_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jonh', 'lee', 'hooker')
print(musician)