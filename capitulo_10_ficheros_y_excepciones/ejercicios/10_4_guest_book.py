# Escribe un bucle que pregunte al usuario por su nombre.
# Cuando introduzca su nombre, imprime un saludo en la pantalla y añade una línea recordándole su visita en un archivo
# llamado guest_book.txt. Asegúrate de que cada entrada aparece en una nueva línea en el fichero.

nombre = input('¿Cuál es tu nombre?: ')
while nombre != '0':
    print(f"Hola {nombre.title()}!")
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(f"Encantados de que nos visites, {nombre.title()}.\n")

    nombre = input('¿Cuál es tu nombre?: ')