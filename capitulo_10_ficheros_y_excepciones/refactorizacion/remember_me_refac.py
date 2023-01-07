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
        print(f"Bienvenido de nuevo, {username}")
    else:
        username = get_new_username()
        print(f"Te recordaremos cuando vuelvas, {username}!")

greet_user()