# Intentamos abrir un archivo que aún no hemos guardado.

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"A ver cómo te lo digo gilipollas, el fichero {filename} no existe.")
