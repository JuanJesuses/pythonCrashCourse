def count_words(filename):
    """Cuenta el número aproximado de palabras en un fichero."""
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

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)