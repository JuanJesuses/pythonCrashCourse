# Haz un diccionario que contenga los tres mayores ríos y el país que atraviesa cada uno.
# Un par clave-valor puede ser ‘nile’:‘egypt’.
#
#     • Utiliza un bucle para imprimir una frase de cada río como, ‘El Nilo recorre Egipto.’
#     • Utiliza un bucle para imprimir el nombre de cada río incluido en el diccionario.
#     • Utiliza un bucle para imprimir el nombre de cada país incluido en el diccionario.

rivers = {
    'nile' : 'egypt',
    'tajo' : 'spain',
    'sena' : 'france',
}

for river, country in rivers.items():
    print(f"El río {river.title()} recorre el país {country.title()}")

print('\n')

for river in rivers.keys():
    print(f"Este es el río {river}")

print('\n')

# Dos opciones para este bucle
# opción 1:
for country in rivers:
    print(f"Este es el país {country}")

print('\n')

# Opción 2:
for country in rivers.values():
    print(f"Este es el país {country}")