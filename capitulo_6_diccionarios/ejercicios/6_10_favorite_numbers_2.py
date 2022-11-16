# Modifica el programa del ejercicio 6-2 para que cada persona pueda tener más de un número favorito.
# Luego imprime el nombre de cada persona con sus números favoritos.

favorite_numbers = {
    'linus' : [24, 14, 38],
    'richard' : [32, 71, 13, 44],
    'alan' :[18, 16, 72],
    'stephen' : [73, 58, 92, 115],
    'guido' : [91, 133, 44, 80],
}

for persona, numeros in favorite_numbers.items():
    print(f"\nLos números favoritos de {persona.title()} son:")
    for numero in numeros:
        print(f"\t{numero}")