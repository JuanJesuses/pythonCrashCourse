# modifica el bloque except del ejercicio 10-8 para que falle silenciosamente si falta alguno de los archivos.

def lee_nombres(filename):

    try:
        with open(filename) as file_object:
            lines = file_object.readlines()

    except FileNotFoundError:
        pass

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