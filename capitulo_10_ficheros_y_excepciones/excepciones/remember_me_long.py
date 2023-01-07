import json

# Carga username si ha sido almacenado previamente.
# En otro caso, solicita el nombre de usuario y lo almacena.

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except:
    username = input("¿Cómo te llamas?: ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"Te recordaremos la próxima ve que vuelvas, {username}!")
else:
    print(f"Bienvenido de nuevo, {username}!")