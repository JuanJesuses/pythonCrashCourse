# Añade una comprobación if a hello_admin.py para asegurarte de que la lista de usuarios no está vacía.

users = []

# 1. Si lo está, imprime el mensaje ‘Necesitamos encontrar algunos usuarios!’.
# 2. Elimina todos los nombres de usuario de tu lista y asegúrate de que el mensaje se imprime correctamente.

if users:
    for user in users:
        if user == 'admin':
            print(f'Hola, {user}, ¿te gustaría ver un informe de estado?')
        else:
            print(f'Hola, {user.title()}, gracias por iniciar sesión nuevamente.')
else:
    print('¡Necesitamos encontrar algunos usuarios!')