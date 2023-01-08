# El listado final de remember_me.py asume que el usuario ya ha introducido su nombre de usuario
# o que el programa se está ejecutando por primera vez.
# Deberíamos modificarlo en caso de que el usuario actual no sea la persona que utilizó el programa por última vez.
# Antes de imprimir un mensaje de bienvenida en greet_user(),
# pregunta al usuario si este es el nombre de usuario correcto.
# Si no lo es, llama a get_new_username() para obtener el nombre de usuario correcto.

import json

def get_stored_username():
    """Obtiene el nombre de usuario si ya está almacenado."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Solicita un nuevo nombre de usuario."""
    username = input("¿Cómo te llamas?: ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Saluda al usuario por su nombre."""
    username = get_stored_username()
    if username:
        print(f"Este es el usuario ya registrado: {username}")
        eres_tu = input("¿Eres tú?(s/n): ")
        if eres_tu == 's':
            print(f"Genial, {username}, no toques mucho los cojones.")
        else:
            username = get_new_username()
            print(f"Te recordaremos cuando vuelvas, {username}!")
    else:
        print("Aún no hay ningún usuario registrado")
        quieres_registro = input("¿Te quieres registrar?(s/n): ")
        if quieres_registro == 's':
            username = get_new_username()
            print(f"Te recordaremos cuando vuelvas, {username}!")
        else:
            print("Pues no des más por culo, gilipollas!")

greet_user()