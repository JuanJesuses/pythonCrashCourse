# Haz lo siguiente para crear un programa que simule como un sitio web comprueba que cada uno
# tiene un nombre de usuario único.

# 1. Haz una lista de cinco o más usuarios llamada current_users.
# 2. Haz otra lista de cinco nombres de usuario llamada new_users.
# Asegúrate de que uno o dos nombres de usuario también están en la lista current_users.
# 3. Recorre la lista new_users para ver si cada nombre de usuario ya se ha utilizado. Si lo ha hecho,
# imprime un mensaje para que la persona introduzca un nuevo nombre de usuario.
# Si el nombre de usuario no ha sido utilizado, imprime un mensaje diciendo que ese nombre está disponible.
# 4. Asegúrate de que tu comparación no distingue entre mayúsculas y minúsculas. Si ‘John’ ya está en uso,
# ‘JOHN’ no es un nombre válido. (Para hacer esto necesitas hacer una copia de current_users
# que contenga una versión en minúsculas de todos los nombres de usuario existentes.)

current_users = ['Alan', 'Richard', 'Linus', 'Guido', 'Howard']
current_users_copy = []

for user in current_users:
    current_users_copy.append(user.lower())

new_users = ['guido', 'juan', 'alvaro', 'alex', 'linus']

for new_user in new_users:
    if new_user in current_users_copy:
        print(f'Lo sentimos, el usuario {new_user.title()} ya existe en el sistema. '
              f'Por favor, escoge otro nombre de usuario.')
    else:
        print(f'El usuario {new_user.title()} está disponible. ¿desea utilizarlo?')
