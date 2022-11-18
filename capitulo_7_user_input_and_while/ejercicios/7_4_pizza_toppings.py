# Escribe un bucle que solicite al usuario proporcionar una serie de ingredientes para pizza
# hasta que introduzca el valor ‘quit’.
# A medida que introduce cada ingrediente, imprime un mensaje que diga que se agregará ese ingrediente a su pizza.

while True:
    pizza_toppings = input('Introduce los ingredientes de tu pizza ("quit" para terminar): ')

    if pizza_toppings != 'quit':
        print(f"Se ha añadido el ingrediente: {pizza_toppings}.")
    else:
        break