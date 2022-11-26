# Comienza con el programa del ejercicio 8-7. Escribe un bucle while que permita a los usuarios introducir
# el álbum de un artista y el título. Una vez que tienes esa información, llama a make_album()
# con la entrada del usuario e imprime el diccionario que se ha creado.
# Asegúrate de incluir un valor quit en el bucle while.

def make_album(artist, album, num_canciones = None):
    if num_canciones:
        disco = {'artista' : artist, 'álbum' : album, 'número canciones' : num_canciones}
        print(disco)
    else:
        disco = {'artista' : artist, 'álbum' : album}
        print(disco)

valor_quit = True

while valor_quit:
    artista = input('Introduzca el nombre del artista: ')
    album = input('Intrduzca el nombre del álbum: ')
    canciones = input('¿Quiere introducur el número de canciones (si/no)?')
    if canciones == 'si':
        num_canciones = int(input('Introduzca el número de canciones: '))
        make_album(artista, album, num_canciones)
    else:
        print('No va a introducir el número de canciones.')
        make_album(artista, album)

    otra_vez = input('¿Quiere introducir otro artista (si/no)?')
    if otra_vez == 'no':
        valor_quit = False

