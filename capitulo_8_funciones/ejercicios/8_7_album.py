# Escribe una función llamada make_album() que construya un diccionario que describa un álbum de música.
# La función debe tomar un nombre de un artista, el título de un álbum y tiene que devolver un diccionario
# que contenga esas dos partes de información. Utiliza la función para hacer tres diccionarios
# que representen diferentes álbumes.
# Imprime cada valor devuelto para mostrar que los diccionarios almacenan correctamente la información del álbum.
# Usa None para añadir un parámetro para que make_album() te permita almacenar el número de canciones en un álbum.
# Si la línea de llamada incluye un valor para el número de canciones, agrega ese valor al diccionario del álbum.
# Haz al menos una nueva llamada a la función que incluya el número de canciones en un álbum.

def make_album(artist, album, num_canciones = None):
    if num_canciones:
        disco = {'artista' : artist, 'álbum' : album, 'número canciones' : num_canciones}
    else:
        disco = {'artista' : artist, 'álbum' : album}
    print(disco)

make_album('paul weller', 'stanley road')
make_album('091', 'todo lo que vendrá después')
make_album('radiohead', 'the bends')
make_album('sonic youth', 'washing machine', 11)

