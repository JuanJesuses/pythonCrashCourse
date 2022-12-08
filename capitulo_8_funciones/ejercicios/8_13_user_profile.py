# Empieza con una copia de user_profile.py del ejemplo anterior.
# Construye un perfil de ti mismo, llamado build_profile(),
# utilizando tu nombre, apellidos y otros tres pares clave-valor que te describan.

def build_profile(first, last, **user_info):
    """ Construye un diccionario que contiene todo lo que sabemos de un usuario. """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('JuanJe', 'Rodriguez', hobbie='python programming', hair_color='red', height='80 Kg.')
print(my_profile)