# Usa un diccionario para almacenar números favoritos de personas.
# Piensa cinco nombres y úsalos como claves de tu diccionario. Piensa en el número favorito de cada persona
# y almacénalo como valor. Imprime el nombre de cada persona y su número favorito.
# Para mayor diversión, sondea algunos amigos y obtén datos reales para tu programa.

favorite_numbers = {
    'linus' : 24,
    'richard' : 32,
    'alan' :18,
    'stephen' : 73,
    'guido' : 91,
}

print(favorite_numbers)

personas = favorite_numbers.keys()

for persona in personas:
    print(f'El número favorito de {persona.title()} es:', favorite_numbers[persona])