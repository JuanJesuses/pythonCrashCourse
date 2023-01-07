import json

def greet_user():
    """Saluda al usuario por su nombre."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("¿Cómo te llamas?: ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"Te recordaremos cuando vuelvas, {username}!")
    else:
        print(f"Bienvenido de nuevo, {username}!")

greet_user()