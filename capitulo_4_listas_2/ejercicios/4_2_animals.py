''' Piensa en al menos tres animales diferentes que tengan caracaterísticas en común. Almacena los nombres de esos
    animales en una lista y utiliza un bucle for para imprimir el nombre de cada animal. '''

animals = ['perro', 'gato', 'culebra']

for animal in animals:
    print(f'{animal.title()}')

# Modifica tu programa para escrbir una frase acerca de cada animal como, 'El perro es una gran mascota'.

animals = ['perro', 'gato', 'culebra']

for animal in animals:
    print(f'El {animal.title()} es una gran mascota.')

# Añade una línea al final del programa indicando lo que estos animales tienen en común. Puedes imprimir una frase como 'Cualquier de
# estos animales podría ser una gran mascota.'

animals = ['perro', 'gato', 'culebra']

for animal in animals:
    print(f'El {animal.title()} es una gran mascota.')
print('¡Cualquiera de estos animales podría ser una gran mascota!')