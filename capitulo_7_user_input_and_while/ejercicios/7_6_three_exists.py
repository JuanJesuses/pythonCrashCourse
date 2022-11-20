# Escribe diferentes versiones de los ejercicios 7-4 o 7-5, para que hagan lo siguiente al menos una vez:
#
#     • Utiliza un test condicional en la instrucción while para detener el bucle.
#     • Utiliza una variable activa para controlar cuánto tiempo se ejecuta el bucle.
#     • Utiliza una sentencia break para salir del bucle cuando el usuario introduzca el valor ‘quit’.

active = True

while active:

    edad = int(input('Introduzca su edad (0 para terminar): '))

    if edad == 0:
        active = False

    if edad > 0 and edad < 3:
        print("Su entrada gratis.")
    elif edad >= 3 and edad < 12:
        print("Su entrada cuesta 10 Euros.")
    elif edad >= 12:
        print("Su entrada cuesta 15 Euros.")

while True:
    pizza_toppings = input('Introduce los ingredientes de tu pizza ("quit" para terminar): ')

    if pizza_toppings != 'quit':
        print(f"Se ha añadido el ingrediente: {pizza_toppings}.")
    else:
        break