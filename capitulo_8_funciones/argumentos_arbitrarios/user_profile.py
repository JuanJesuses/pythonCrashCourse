def build_profile(first, last, **user_info):
    """ Construye un diccionario que contiene todo lo que sabemos de un usuario. """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)