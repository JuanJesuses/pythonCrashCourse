# Lee en cada línea del nuevo fichero que acabas de crear, learning_python.txt
# y cambia la palabra Python por el nombre de otro lenguaje como C. Imprime por pantalla cada línea modificada.

filename = ('learning_python.txt')

with open(filename) as file_object:
    learn = file_object.readlines()

list_file = ''

for line in learn:
    list_file += line

if 'Python' in list_file:

    list_file.replace('Python', 'C') # Esto reemplaza pero no persiste
    print(f"{list_file}\n") # Se imprime el archivo original

    c_file = list_file.replace('Python', 'C') # Hqy eu asignar a una variable para que persistan lso cambios.
    print(c_file)