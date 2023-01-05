# Intentamos abrir un archivo que aún no hemos guardado.

filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()