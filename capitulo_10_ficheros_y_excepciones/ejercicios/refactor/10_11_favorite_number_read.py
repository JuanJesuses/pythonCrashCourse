import json

filename = 'numero_f.json'

with open(filename) as f:
    numero = json.load(f)
    #print(f"Tu número favorito es: {json.load(f)}.")

print(f"Tu número favorito es: {numero}!")