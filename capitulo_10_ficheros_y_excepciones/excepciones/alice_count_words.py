# Contaremos el número de palabras que contiene el libro Alice in Wonderland

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"A ver cómo te lo digo gilipollas, el fichero {filename} no existe.")
else:
    # Contamos el número aproximado de palabras del fichero.
    words = contents.split()
    num_words = len(words)
    print(f"Comemierdas, el fichero {filename} tiene más o menos {num_words} palabras.\n"
          f"Más o menos, joder que lo quieres saber todo.")