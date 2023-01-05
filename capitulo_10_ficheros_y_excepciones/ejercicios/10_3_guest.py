# Escribe un programa que pregunte al usuario por su nombre.
# Cuando responda, escribe su nombre en un fichero llamado guest.txt.

nombre = input('¿Cuál es tu nombre?: ')

with open('guest.txt', 'a') as file_object:
    file_object.write(nombre)
