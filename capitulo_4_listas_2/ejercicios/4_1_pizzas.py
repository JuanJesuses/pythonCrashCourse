''' Piensa al menos tres tipos de pizzas que sean tus favoritas. Almacena esos nombres de pizza en una lista, y luego
    utiliza un bucle for para imprimir el nombre de cada pizza. '''

names_of_pizza = ['margarita', 'cuatro quesos', 'diavola', 'calzone']

for pizza in names_of_pizza:
    print(f'{pizza.title()}.')

# Utiliza tu bucel for para imprimir una frase utilizando el nombre de la pizza en lugar de utilizar śolamente
# el nombre de la pizza. Por cada pizza podrías imprimir una línea que contenga una frase sencilla
# como 'Me gusta la pizza calzone'.

names_of_pizza = ['margarita', 'cuatro quesos', 'diavola', 'calzone']

for pizza in names_of_pizza:
    print(f'Me gusta la pizza tipo {pizza.title()}.')


# Añade una línea al final de tu programa, fuera del bucle, que diga lo mucho que te gusta la pizza.

names_of_pizza = ['margarita', 'cuatro quesos', 'diavola', 'calzone']

for pizza in names_of_pizza:
    print(f'pizza tipo {pizza.title()}.')
print('Realmente me encanta la pizza!!!')