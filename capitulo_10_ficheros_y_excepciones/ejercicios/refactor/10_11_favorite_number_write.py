# Escribe un programa que pida al usuario su número favorito. Usa json.dump() para almacenar este número en un archivo.
# Escribe un programa separado que lea en este valor e imprima el mensaje: “Se tu número favorito!, es___”.
import json

num_fav = input("¿Cuál es tu número favorito?: ")
filename = 'numero_f.json'

with open(filename, 'w') as f:
    json.dump(int(num_fav), f)