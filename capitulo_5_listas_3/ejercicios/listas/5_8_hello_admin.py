# Haz una lista de cinco o más usuarios, incluyendo el nombre ‘admin’.
# Imagina que estás imprimiendo un código que imprimirá un saludo a cada usuario después de que se
# identifiquen en un sitio web. El bucle recorrerá la lista e imprimirá un saludo a cada usuario:

users = ['admin', 'richard', 'linus', 'guido', 'howard']

# 1. Si el usuario es ‘admin’, imprime un saludo especial como ‘Hola admin, ¿te gustaría ver un informe de estado?’
for user in users:
    if user == 'admin':
        print(f'Hola, {user}, ¿te gustaría ver un informe de estado?')
# 2. De lo contrario imprime un saludo genérico como ‘Hola Jaden, gracias por iniciar sesión nuevamente.’
    else:
        print(f'Hola, {user.title()}, gracias por iniciar sesión nuevamente.')
