# Haz dos ficheros, cats.txt y dogs.txt. Almacena al menos tres nombres de gatos en el primer fichero
# y tres nombres de perro en el segundo. Escribe un programa que intente leer esos ficheros
# e imprima el contenido por pantalla.
# Envuelve tu código en un bloque try-except para capturar un error de archivo no encontrado (FileNotFoundError)
# e imprime un mensaje amigable si el archivo está perdido.
# Mueve uno de los archivos a una ubicación diferente en tu equipo y asegúrate de que el código del bloque except
# se ejecuta correctamente.

def lee_nombres(filename):

    try:
        with open(filename) as file_object:
            lines = file_object.readlines()

    except FileNotFoundError:
        print("Vamos a ver, imbécil, que el archivo no está aquí!!")

    else:
        if filename == 'cats.txt':
            print('Los nombres de los gatillos son: ')
        else:
            print("\nLos nombres de los perrillos son: ")
        for line in lines:
            print(line.strip().title())

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    lee_nombres(filename)