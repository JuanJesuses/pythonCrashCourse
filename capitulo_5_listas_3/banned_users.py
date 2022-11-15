# Comprobar si un usuario de un sitio web ha sido baneado.

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, puedes publicar una respuesta si lo deseas.')