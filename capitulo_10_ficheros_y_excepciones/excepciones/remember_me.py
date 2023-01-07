import json

usename = input('Introduce tu nombre: ')

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(usename, f)
    print(f"Te recordaremos cuando vuelvas,  {usename}")