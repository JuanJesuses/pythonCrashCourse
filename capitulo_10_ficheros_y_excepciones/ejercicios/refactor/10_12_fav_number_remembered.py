# Combina los dos programas del ejercicio 10-11 en un fichero. Si el número ya está almacenado,
# informa al usuario del número favorito.
# Si no lo está, solicita el usuario su número favorito y almacénalo en un archivo.
# Ejecuta el programa dos veces para ver si funciona.
import json

filename = 'numero_fav.json'

try:
    with open(filename) as f:
        num_fav = json.load(f)
except FileNotFoundError:
    num_fav = int(input("¿Cuál es tu número favorito?: "))
    with open(filename, 'w') as f:
        json.dump(num_fav, f)
        print(f"Recordaremos la próxima vez que tu número favorito es: {num_fav}!")
else:
    print(f"Tu número favorito es: {num_fav}!")